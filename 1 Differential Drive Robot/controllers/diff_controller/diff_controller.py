from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice("motor2")
right_motor = robot.getDevice("motor1")

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

speed = 2.0
left_motor.setVelocity(speed)
right_motor.setVelocity(speed)

while robot.step(timestep) != -1:
    pass