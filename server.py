from flask import Flask, render_template
from denon import Denon

app = Flask(__name__)
denon_device = None  # Will be initialized in main.py

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pw/<action>")
def power(action):
    if action == "on":
        result = denon_device.powerOn()
    elif action == "off":
        result = denon_device.powerOff()
    elif action == "status":
        result = denon_device.powerStat()
    else:
        result = "Invalid action"
    return render_template("result.html", result=result)

@app.route("/vol/<action>")
def volume(action):
    if action == "up":
        result = denon_device.volUp()
    elif action == "down":
        result = denon_device.volDown()
    else:
        result = "Invalid action"
    return render_template("result.html", result=result)

@app.route("/mute/<action>")
def mute(action):
    if action == "on":
        result = denon_device.muteOn()
    elif action == "off":
        result = denon_device.muteOff()
    elif action == "status":
        result = denon_device.muteStat()
    else:
        result = "Invalid action"
    return render_template("result.html", result=result)
