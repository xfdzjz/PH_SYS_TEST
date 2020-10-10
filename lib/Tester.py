import serial
from time import sleep

class Tester:
    def __init__(self, config):
        self.port = serial.Serial(config["port"], config["baudRate"],timeout=2,inter_byte_timeout=0.2)
        # self.port = serial.Serial(config["port"], config["baudRate"],timeout=2)

    def __del__(self):
        try:
            self.port.close()
        except:
            pass

    def stopAll(self):
        pass

    def runCommand(self, cmd, timeout=None):# communication using serial port and how much string number will be read
        self.port.flushInput()
        print("RUNCMD: %s" % cmd)
        buffer = (cmd + " ").encode('ascii')
        self.port.write(buffer) # command ending char " "
        if timeout:
            self.port.timeout = timeout
            # sleep(timeout)
        else:
            # sleep(0.2)
            self.port.timeout = 2
        readVal = self.port.read(100)
        # readVal = self.port.read_all()
        val = readVal.decode("ascii")
        print("RESP: %s(%d)" % (val, len(val)) )
        return val

    def readsn(self):
        self.port.write(("ReadSN"+' ').encode('ascii'))
        sleep(0.2)
        readVal = self.port.read_all()
        val = readVal.decode("ascii")
        return val


    def waitResponse(self):
        pass

if __name__ == "__main__":
    # Unit test
    t = Tester({"port": "COM10", "baudRate": 115200})
    ERROR_OK = t.runCommand(("test_vdd_stable"))
    print(ERROR_OK)
    ERROR_OK = t.runCommand(("open_power_en"))
    print(ERROR_OK)
    ERROR_OK = t.runCommand(("test_cmp"))
    print(ERROR_OK)
    print("do some unittest")
    input("Press ENTER to continue")
    print("do some unittest")
    print("PASS")
