from controller import Robot, Keyboard
import cv2
import numpy as np

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def main():
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    # Keyboard for manual control
    keyboard = Keyboard()
    keyboard.enable(timestep)

    # Motors to control the Hinge2Joint
    motor1 = robot.getDevice("axis1motor")  # pan
    motor2 = robot.getDevice("axis2motor")  # tilt
    motor1.setPosition(0)
    motor2.setPosition(0)

    # Get camera by name (make sure name exists in world file)
    camera = robot.getDevice("camera")
    camera.enable(timestep)
    width = camera.getWidth()
    height = camera.getHeight()

    # Initial angles
    pan_angle = 0.0
    tilt_angle = 0.0
    pan_limit = 1.57
    tilt_limit = 1.3
    step = 0.05

    while robot.step(timestep) != -1:
        key = keyboard.getKey()

        if key == ord('A'):
            pan_angle += step
        elif key == ord('D'):
            pan_angle -= step
        elif key == ord('W'):
            tilt_angle += step
        elif key == ord('S'):
            tilt_angle -= step

        pan_angle = clamp(pan_angle, -pan_limit, pan_limit)
        tilt_angle = clamp(tilt_angle, -tilt_limit, tilt_limit)

        motor1.setPosition(pan_angle)
        motor2.setPosition(tilt_angle)

        # Read camera image and convert to OpenCV format
        image = camera.getImage()
        if image:
            img_array = np.frombuffer(image, dtype=np.uint8).reshape((height, width, 4))
            img_bgr = cv2.cvtColor(img_array, cv2.COLOR_BGRA2BGR)

            # Display live feed
            cv2.imshow("Webots Camera Feed", img_bgr)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        print(f"Pan: {pan_angle:.2f}, Tilt: {tilt_angle:.2f}")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
