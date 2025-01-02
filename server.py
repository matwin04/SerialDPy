from flask import * 
from denon import Denon

app = Flask(__name__)
def getDevice():
    port = "/dev/ttyUSB0"
    baudRate = 9600
    return Denon(port,baudRate)
device = getDevice()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pw/<action>")
def power(action):
    if action == "on":
        result = device.powerOn()
    elif action == "off":
        result = device.powerOff()
    elif action == "status":
        result = device.powerStat()
    else:
        result = "Invalid action"
    return redirect("/")

@app.route("/vol/<action>")
def volume(action):
    if action == "up":
        result = device.volUp()
    elif action == "down":
        result = device.volDown()
    else:
        result = "Invalid action"
    return redirect("/")

@app.route("/mute/<action>")
def mute(action):
    if action == "on":
        result = device.muteOn()
    elif action == "off":
        result = device.muteOff()
    elif action == "status":
        result = device.muteStat()
    else:
        result = "Invalid action"
    return redirect("/")