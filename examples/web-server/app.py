import time
from flask import Flask, render_template
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()
app = Flask(__name__)


def forward():
    robot.forward()
    time.sleep(1)
    robot.stop()


def backward():
    robot.backward()
    time.sleep(1)
    robot.stop()


def left():
    robot.left()
    time.sleep(1)
    robot.stop()


def right():
    robot.right()
    time.sleep(1)
    robot.stop()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<action>")
def action(action):
    if action == "forward":
        forward()
    if action == "backward":
        backward()
    if action == "left":
        left()
    if action == "right":
        right()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
