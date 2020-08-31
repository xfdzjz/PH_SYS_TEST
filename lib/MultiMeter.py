class MultiMeter:
    def __init__(self, config):
        self.config = config

    def stopAll(self):
        # 复位到待接线状态
        pass

    def getVoltage(self):
        return 0

    def getCurrent(self):
        return 0



if __name__ == "__main__":
    # Unit test
    m = MultiMeter({})
    print("do some unittest")
    input("Press ENTER to continue")
    print("do some unittest")
    print("PASS")
