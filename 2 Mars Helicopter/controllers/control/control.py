from controller import Supervisor

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

motor = robot.getDevice("motor top")
motor.setPosition(float('inf'))
motor.setVelocity(50)

body = robot.getFromDef("MARS_HELICOPTER")  # Or "MARS_HELICOPTER" if you DEF the Robot node

while robot.step(timestep) != -1:
    thrust = 4.66 # Hover level
    if body:
        body.addForce([0, 0, thrust], False)
