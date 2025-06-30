from controller import Supervisor

def main():
    robot = Supervisor()
    timestep = int(robot.getBasicTimeStep())

    quad = robot.getFromDef("QUADCOPTER")

    motor_names = ["motor 1", "motor 2", "motor 3", "motor 4"]
    motors = {name: robot.getDevice(name) for name in motor_names}
    for motor in motors.values():
        motor.setPosition(float('inf'))

    # Constants
    mass = 0.58
    g = 9.81
    hover_thrust = mass * g / 4

    k_thrust = (hover_thrust / 50.0)
    k_yaw_torque = 0.001  # Higher value for faster yaw

    L = 0.1
    h = 0.047

    offsets = {
        "motor 1": [-L, -L, h],
        "motor 2": [-L,  L, h],
        "motor 3": [ L,  L, h],
        "motor 4": [ L, -L, h],
    }

    spin_dir = {
        "motor 1": 1,
        "motor 2": -1,
        "motor 3": 1,
        "motor 4": -1
    }

    inputs = {
        "motor 1": 50.5,
        "motor 2": 50.5,
        "motor 3": 50.5,
        "motor 4": 50.5
    }

    while robot.step(timestep) != -1:
        total_torque = [0.0, 0.0, 0.0]  # pitch, roll, yaw

        for name, percent in inputs.items():
            thrust = percent * k_thrust
            offset = offsets[name]
            force = [0, 0, thrust]

            # Apply force
            quad.addForceWithOffset(force, offset, False)

            # Torque = r × F
            torque_pitch = offset[0] * thrust
            torque_roll = offset[1] * thrust
            total_torque[0] += torque_pitch
            total_torque[1] += torque_roll
            total_torque[2] += spin_dir[name] * percent * k_yaw_torque

            motors[name].setVelocity(percent)

        quad.addTorque(total_torque, False)

if __name__ == "__main__":
    main()
