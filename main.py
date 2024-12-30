from server import app
from denon import Denon

def main():
    global denon_device
    port = "/dev/ttyUSB0"
    denon_device = Denon(port)
    app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
