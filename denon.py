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
    #Mute
    def muteOn(self):
        self.sendCommand("MUON")
    def muteOff(self):
        self.sendCommand("MUOFF")
    def muteStat(self):
        self.sendCommand("MU?")

    #Source Selector
    def selPhono(self):
        self.sendCommand("SIPHONO")
    def selCD(self):
        self.sendCommand("SICD")
    def selTuner(self):
        self.sendCommand("SITUNER")
    def selDVD(self):
        self.sendCommand("SIDVD")
    def selTV(self):
        self.sendCommand("SITV/CBL")
    def selVCR(self):
        self.sendCommand("SIVCR")
    def selDVR(self):
        self.sendCommand("SIDVR")
    def selVAUX(self):
        self.sendCommand("SIV.AUX")
    def selXM(self):
        self.sendCommand("SIXM")
    def selIPod(self):
        self.sendCommand("SIIPOD")
    def selAUX(self):
        self.sendCommand("SIAUX")
    def inputStatus(self):
        self.sendCommand("SI?")
    
    #Record Selector
    def recSelPhono(self):
        self.sendCommand("SRPHONO")
    def recSelCD(self):
        self.sendCommand("SRCD")
    def recSelTuner(self):
        self.sendCommand("SRTUNER")
    def recSelDVD(self):
        self.sendCommand("SRDVD")
    def recSelTV(self):
        self.sendCommand("SRTV/CBL")
    def recSelVCR(self):
        self.sendCommand("SRVCR")
    def recSelDVR(self):
        self.sendCommand("SRDVR")
    def recSelVAUX(self):
        self.sendCommand("SRVAUX")
    def recSelXM(self):
        self.sendCommand("SRXM")
    def recSelIPOD(self):
        self.sendCommand("SRIPOD")
    def recSelAUX(self):
        self.sendCommand("SRAUX")
    def recModeCancel(self):
        self.sendCommand("SRSOURCE")
    #Video Scale
    def vssc48p(self):
        self.sendCommand("VSSC48P")
    def vssc10i(self):
        self.sendCommand("VSSC10I")
    def vssc10p(self):
        self.sendCommand("VSSC10P")
    def vssc72p(self):
        self.sendCommand("VSSC72P")