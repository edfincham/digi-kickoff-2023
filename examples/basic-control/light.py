import time
from gpiozero import LineSensor

# Define GPIO pin
pinLineFollower = 25

sensor = LineSensor(pinLineFollower)


def lineseen():
    print("Line seen")


def linenotseen():
    print("No line seen")


sensor.when_line = lineseen

sensor.when_no_line = linenotseen

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    exit()
