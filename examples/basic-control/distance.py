import time
from gpiozero import DistanceSensor

# Define GPIO pins
pintrigger = 17
pinecho = 18

sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

try:
    while True:
        print("Distance: %.3f cm" % (sensor.distance * 100))
        time.sleep(0.5)
except KeyboardInterrupt:
    exit()
