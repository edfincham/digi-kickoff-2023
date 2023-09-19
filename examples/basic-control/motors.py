import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

robot.forward()
time.sleep(2)

robot.backward()
time.sleep(2)

robot.stop()
