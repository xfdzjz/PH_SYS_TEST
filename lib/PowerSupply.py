import visa


class PowerSupply:
    def __init__(self, config):
        rm = visa.ResourceManager()
        inst = rm.open_resource(config["port"])
        self.inst = inst

    def __del__(self):
        self.inst.close()

    def stopAll(self):
        # 复位到待接线状态
        self.inst.write(":OUTPut1:STATe OFF")
        self.inst.write(":OUTPut2:STATe OFF")
        self.inst.write(":OUTPut3:STATe OFF")
        self.inst.write(":OUTPut4:STATe OFF")

    def voltageOutput(self, channel, V, I, ovp, ocp):
        self.inst.write(":OUTPut%d:STATe ON" % (channel))
        self.inst.write(":OUTPut%d:OCP:STATe ON" % channel)
        self.inst.write(":OUTPut%d:OVP:STATe ON" % channel)
        self.inst.write(":OUTPut%d:OVP %f" % (channel, ovp))
        self.inst.write(":OUTPut%d:OCP %f" % (channel, ocp))
        self.inst.write("ISET%d:%f" % (channel, I))
        self.inst.write("VSET%d:%f" % (channel, V))


if __name__ == "__main__":
    # Unit test
    ps = PowerSupply({"port": "COM4"})
    ps.stopAll()
    input("Press ENTER to continue")
    ps.voltageOutput(2, 2, 0.1, 3, 1)
    print("PASS")
