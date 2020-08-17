import serial
from time import sleep


class Tester:
    def __init__(self, config):
        self.port = serial.Serial(
            config["port"], config["baudRate"], timeout=2)

    def __del__(self):
        self.port.close()

    def stopAll(self):
        # 复位到待接线状态
        pass

    # communication using serial port and how much string number will be read
    def runCommand(self, cmd):

        self.port.write((cmd + " ").encode('ascii'))  # command ending char " "
        sleep(0.2)
        readVal = self.port.read_all()
        val = readVal.decode("ascii")
        return val

    def waitResponse(self):
        pass


if __name__ == "__main__":
    # Unit test
    t = Tester({"port": "COM6", "baudRate": 9600})
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
