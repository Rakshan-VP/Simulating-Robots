from controller import Supervisor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel
from PyQt5.QtCore import Qt, QTimer
import threading
import sys

# Global variables
motor_speed = 15  # initial motor speed (percent)
running = False

def create_gui():
    window = QWidget()
    window.setWindowTitle("Mars Helicopter Control")

    layout = QVBoxLayout()

    label = QLabel(f"Motor Speed: {motor_speed}%")
    layout.addWidget(label)

    slider = QSlider(Qt.Horizontal)
    slider.setMinimum(0)
    slider.setMaximum(100)
    slider.setValue(motor_speed)
    layout.addWidget(slider)

    button = QPushButton("Start Helicopter")
    layout.addWidget(button)

    def update_label():
        label.setText(f"Motor Speed: {slider.value()}%")

    def start_clicked():
        global running
        running = True

    button.clicked.connect(start_clicked)
    slider.valueChanged.connect(lambda: [update_label(), update_motor_speed(slider)])

    window.setLayout(layout)
    window.show()
    return window

def update_motor_speed(slider):
    global motor_speed
    motor_speed = slider.value()

def webots_controller():
    global motor_speed, running

    robot = Supervisor()
    timestep = int(robot.getBasicTimeStep())

    motor_top = robot.getDevice("motor top")
    motor_bottom = robot.getDevice("motor bottom")

    motor_top.setPosition(float('inf'))
    motor_bottom.setPosition(float('inf'))

    body = robot.getFromDef("MARS_HELICOPTER")

    mass = 0.5  
    g = 9.81
    hover_thrust = mass * g  

    while robot.step(timestep) != -1:
        if running:
            velocity = motor_speed  # 0–100 percent
            motor_top.setVelocity(velocity)
            motor_bottom.setVelocity(velocity)

            thrust = ((velocity / 50) ** 2) * hover_thrust if velocity > 0 else 0
            if body:
                body.addForce([0, 0, thrust], False)

def main():
    app = QApplication(sys.argv)

    # Start Webots in a separate thread
    t = threading.Thread(target=webots_controller)
    t.start()

    window = create_gui()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
