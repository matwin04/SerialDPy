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
    try:
        device.inputStatus()
        currentSource = "Input Status Command sent"
    except Exception as e:
        currentSource = f"Error fetching source status {e}"

    return render_template("index.html",currentSource=currentSource)

@app.route("/power/<action>")
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
@app.route("/source/<source>")
def selectSource(source):

    if source == "PHONO":
        result = device.selPhono()
    elif source == "CD":
        result = device.selCD()
    elif source == "TUNER":
        result = device.selTuner()
    elif source == "DVD":
        result = device.selDVD()
    elif source == "TV+CBL":
        result = device.selTV()
    elif source == "VCR":
        result = device.selVCR()
    elif source == "DVR":
        result = device.selDVR()
    elif source == "VAUX":
        result = device.selVAUX()
    elif source == "XM":
        result = device.selXM()
    elif source == "IPod":
        result = device.selIPod()
    elif source == "AUX":
        result = device.selAUX()
    else:
        result = "Invalid Action"
    return redirect("/")
@app.route("/record/<source>")
def recSelectSource(source):
    if source == "PHONO":
        result = device.recSelPhono()
    elif source == "CD":
        result = device.recSelCD()
    elif source == "TUNER":
        result = device.recSelTuner()
    elif source == "DVD":
        result = device.recSelDVD()
    elif source == "TV+CBL":
        result = device.recSelTV()
    elif source == "VCR":
        result = device.recSelVCR()
    elif source == "DVR":
        result = device.recSelDVR()
    elif source == "VAUX":
        result = device.recSelVAUX()
    elif source == "IPOD":
        result = device.recSelIPOD()
    elif source == "AUX":
        result = device.recSelAUX()
    elif source == "CANCEL":
        result = device.recModeCancel()
    else:
        result = "Invalid Selection"
    return redirect("/")