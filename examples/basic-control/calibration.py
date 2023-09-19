import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.4
rightmotorspeed = 0.6

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)

robot.value = motorforward
time.sleep(1)

robot.value = motorbackward
time.sleep(1)

robot.value = motorleft
time.sleep(1)

robot.value = motorright
time.sleep(1)

robot.stop()
