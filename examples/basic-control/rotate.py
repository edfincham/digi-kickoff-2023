import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

robot.left()
time.sleep(2)

robot.right()
time.sleep(2)

robot.stop()
