from controller import Supervisor
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QHBoxLayout, QGridLayout, QLineEdit
)
from PyQt5.QtCore import Qt
import sys, threading

# Global variables
desired_altitude = 1.0  # meters
kp, ki, kd = 5.0, 0.0, 2.0
integral = 0
last_error = 0
height_sensor_offset = 0.203
running = False
labels = {}

def create_gui():
    window = QWidget()
    window.setWindowTitle("Mars Helicopter Altitude Controller")

    layout = QVBoxLayout()
    grid = QGridLayout()

    # Input fields
    desired_input = QLineEdit(str(desired_altitude))
    grid.addWidget(QLabel("Desired Altitude (m):"), 0, 0)
    grid.addWidget(desired_input, 0, 1)

    for i, name in enumerate(["Kp", "Ki", "Kd"], 1):
        labels[name] = QLineEdit(str(globals()[name.lower()]))
        grid.addWidget(QLabel(name + ":"), i, 0)
        grid.addWidget(labels[name], i, 1)

    layout.addLayout(grid)

    # Status display
    labels["altitude"] = QLabel("Current Altitude: 0.00 m")
    labels["thrust"] = QLabel("Thrust: 0 N")
    labels["throttle"] = QLabel("Throttle: 0%")
    for lbl in ["altitude", "thrust", "throttle"]:
        layout.addWidget(labels[lbl])

    # Buttons
    button_layout = QHBoxLayout()
    start_btn = QPushButton("Start")
    stop_btn = QPushButton("Stop")
    button_layout.addWidget(start_btn)
    button_layout.addWidget(stop_btn)
    layout.addLayout(button_layout)

    def start_clicked():
        global running, kp, ki, kd, desired_altitude, integral, last_error
        kp = float(labels["Kp"].text())
        ki = float(labels["Ki"].text())
        kd = float(labels["Kd"].text())
        desired_altitude = float(desired_input.text())
        integral = 0
        last_error = 0
        running = True

    def stop_clicked():
        global running
        running = False

    start_btn.clicked.connect(start_clicked)
    stop_btn.clicked.connect(stop_clicked)

    window.setLayout(layout)
    window.show()
    return window

def webots_controller():
    global integral, last_error

    robot = Supervisor()
    timestep = int(robot.getBasicTimeStep())

    sensor = robot.getDevice("height sensor")
    sensor.enable(timestep)

    motor_top = robot.getDevice("motor top")
    motor_bottom = robot.getDevice("motor bottom")
    motor_top.setPosition(float('inf'))
    motor_bottom.setPosition(float('inf'))

    body = robot.getFromDef("MARS_HELICOPTER")
    mass = 0.5
    g = 9.81
    hover_thrust = mass * g

    while robot.step(timestep) != -1:
        height = sensor.getValue() - height_sensor_offset
        labels["altitude"].setText(f"Current Altitude: {height:.3f} m")

        if running:
            error = desired_altitude - height
            dt = timestep / 1000.0
            integral += error * dt
            derivative = (error - last_error) / dt
            last_error = error

            pid = kp * error + ki * integral + kd * derivative
            thrust = max(0, hover_thrust + pid)
            throttle = min(max(thrust / (2 * hover_thrust) * 100, 0), 100)

            labels["thrust"].setText(f"Thrust: {thrust:.2f} N")
            labels["throttle"].setText(f"Throttle: {throttle:.1f}%")

            motor_top.setVelocity(throttle / 2)
            motor_bottom.setVelocity(throttle / 2)

            if body:
                body.addForce([0, 0, thrust], False)
        else:
            motor_top.setVelocity(0)
            motor_bottom.setVelocity(0)
            labels["thrust"].setText("Thrust: 0 N")
            labels["throttle"].setText("Throttle: 0%")

def main():
    app = QApplication(sys.argv)
    thread = threading.Thread(target=webots_controller)
    thread.start()
    gui = create_gui()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
