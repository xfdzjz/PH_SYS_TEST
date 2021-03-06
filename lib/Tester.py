import serial
from time import sleep

class Tester:
    def __init__(self, config):
        self.port = serial.Serial(config["port"], config["baudRate"],timeout=2,inter_byte_timeout=0.2)
        self.SN = ""

    def __del__(self):
        try:
            self.port.close()
        except:
            pass

    def stopAll(self):
        pass

    def runCommand(self, cmd, timeout=None):
        # 读SN小把戏
        if cmd == 'test_mode_sel':
            self.SN = self.runCommand("cReadSN",2)
        elif cmd == 'EnterEstMode':
            #self.SN = self.runCommand("ReadSN",2)
            pass

        self.port.close()
        self.port.open()
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
        print("RESP: ", readVal )
        val = ""
        try:
            val = readVal.decode("ascii")
        except:
            pass
        return val

    def runC(self, cmd, timeout=None):# communication using serial port and how much string number will be read

        buffer = (cmd + " ").encode('ascii')
        self.port.write(buffer) # command ending char " "

    def readsn(self):
        self.port.write(("cReadSN ").encode('ascii'))
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
