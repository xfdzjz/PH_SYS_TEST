import visa
import time

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

    def voltageOutput(self, channel, V, I, ovp, ocp): #open one channel
        self.inst.write(":OUTPut%d:STATe ON" % (channel))
        self.inst.write(":OUTPut%d:OCP:STATe ON" % channel)
        self.inst.write(":OUTPut%d:OVP:STATe ON" % channel)
        self.inst.write(":OUTPut%d:OVP %f" % (channel, ovp))
        self.inst.write(":OUTPut%d:OCP %f" % (channel, ocp))
        self.inst.write("ISET%d:%f" % (channel, I))
        self.inst.write("VSET%d:%f" % (channel, V))

    def resistor(self,channel,ohm, ovp, ocp):
        self.inst.write(":LOAD%d:CR ON " %(channel))
        self.inst.write(":LOAD%d:CV OFF " %(channel))
        self.inst.write(":LOAD%d:CC OFF " %(channel))
        #self.inst.write(":OUTPut:SERies ON")
        #self.inst.write(":OUTPut%d:OCP:STATe ON" % channel)
        #self.inst.write(":OUTPut%d:OVP:STATe ON" % channel)
        #self.inst.write(":OUTPut%d:OVP %f" % (channel, ovp))
        #self.inst.write(":OUTPut%d:OCP %f" % (channel, ocp))
        self.inst.write(":LOAD%d:RESistor %f" %(channel,ohm))
        #self.inst.write(":SOURce%d:RESistor %f"  %(channel,ohm))
        print(self.inst.query(":LOAD%d:RESistor?"%(channel)))
        #print(self.inst.query(":SOURce%d:RESistor?"%(channel)))
        print(ohm)

    def measure(self,channel,IV):
        self.inst.write(":LOAD%d:CR ON " %(channel))
        if IV == "CURRent":
            self.inst.write(":MEASure%d:CURRent? " %channel)
            cur = self.inst.query(":IOUT%d?" %channel)
            print(cur)
            return cur
        if IV == "vol":
            vol = self.inst.query(":MEASure%d:VOLTage? " %channel)
            return vol

    def channelOn(self,channel):
        self.inst.write(":OUTPut%d:STATe ON" %channel)

    def channelOff(self,channel):
        self.inst.write(":OUTPut%d:STATe OFF" %channel)




if __name__ == "__main__":
    # Unit test
    ps = PowerSupply({"port": "COM4"})
    ps.stopAll()
    input("Press ENTER to continue")
    ps.voltageOutput(2, 2, 0.1, 3, 1)
    print("PASS")
