from denon import Denon
def main():
    port = "/dev/ttyUSB0"
    denon = Denon(port)
    denon.close()
if __name__ == "__main__":
    main()