from controller import Robot

def main():
    # Create the robot instance
    robot = Robot()
    
    # Get the simulation timestep (ms)
    timestep = int(robot.getBasicTimeStep())
    
    # Get the GPS device
    gps = robot.getDevice("gps")
    gps.enable(timestep)

    while robot.step(timestep) != -1:
        # Get GPS position (x, y, z)
        position = gps.getValues()
        print(f"GPS Position: x={position[0]:.3f}, y={position[1]:.3f}, z={position[2]:.3f}")

if __name__ == "__main__":
    main()
