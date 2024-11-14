import serial
class Denon:
    def __init__(self,port:str,baudrate: int = 9600):
        try:
            self.ser = serial.Serial(port,baudrate,timeout=1)
        except serial.SerialException as e:
            print(f"Error opening serial port : {e}")
            raise
    def sendCommand(self,command:str):
        cmd = f"{command}\r"
        try:
            self.ser.write(cmd.encode())
        except serial.SerialException as e:
            print(f"Error writing to serial port : {e}")
    #Power
    def powerOn(self):
        self.sendCommand("PWON")
    def powerOff(self):
        self.sendCommand("PWSTANDBY")
    def powerStat(self):
        self.sendCommand("PW?")
    #Master Volume
    def volUp(self):
        self.sendCommand("MVUP")
    def volDown(self):
        self.sendCommand("MVDOWN")

    def close(self):
        self.ser.close()