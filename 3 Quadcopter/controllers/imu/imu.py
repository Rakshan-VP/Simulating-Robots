from controller import Robot
import math

# Create robot instance
robot = Robot()

# Get the simulation timestep
timestep = int(robot.getBasicTimeStep())

# Get the InertialUnit device
imu = robot.getDevice("imu")
imu.enable(timestep)

# Main loop
while robot.step(timestep) != -1:
    # Get roll, pitch, yaw from the IMU
    rpy = imu.getRollPitchYaw()

    # Convert radians to degrees (optional)
    roll_deg = math.degrees(rpy[0])
    pitch_deg = math.degrees(rpy[1])
    yaw_deg = math.degrees(rpy[2])

    # Print the values
    print(f"Roll: {roll_deg:.2f}°, Pitch: {pitch_deg:.2f}°, Yaw: {yaw_deg:.2f}°")
