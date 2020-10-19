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
        for channel in range(1,5):
            self.inst.write(":OUTPut%d:STATe ON" % (channel))
            self.inst.write(":OUTPut%d:OCP:STATe ON" % channel)
            self.inst.write(":OUTPut%d:OVP:STATe ON" % channel)
            self.inst.write(":OUTPut%d:OVP %f" % (channel, 12))
            self.inst.write(":OUTPut%d:OCP %f" % (channel, 1))
            self.inst.write("ISET%d:%f" % (channel, 0.2))
            self.inst.write(":OUTPut%d:STATe OFF"% (channel))

    def voltageOutput(self, channel, V, I, ovp, ocp): #open one channel
        # print("Try set voltage to %f:%f:%f:%f" % (V ,I, ovp, ocp))
        self.inst.write(":OUTPut%d:STATe ON" % (channel))
        # self.inst.write(":OUTPut%d:OCP:STATe ON" % channel)
        # self.inst.write(":OUTPut%d:OVP:STATe ON" % channel)
        # self.inst.write(":OUTPut%d:OVP %f" % (channel, ovp))
        # self.inst.write(":OUTPut%d:OCP %f" % (channel, ocp))
        # self.inst.write("ISET%d:%f" % (channel, I))
        self.inst.write("VSET%d:%f" % (channel, V))
        time.sleep(0.3) # 等待 300ms 电压正常输出

    def resistor(self,channel,ohm, ovp, ocp):
        self.inst.write(":OUTPut%d:STATe ON" % (channel))
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
        self.inst.write(":OUTPut%d:STATe ON" % (channel))
        self.inst.write(":LOAD%d:CR ON " %(channel))
        if IV == "CURRent":
            self.inst.write(":MEASure%d:CURRent? " %channel)
            cur = self.inst.query(":IOUT%d?" %channel)
            cur = cur[:-2]
            print(cur)
            return float(cur)
        if IV == "vol":
            vol = self.inst.query(":MEASure%d:VOLTage?" %channel)
            return float(vol)

    def channelOn(self,channel):
        self.inst.write(":OUTPut%d:STATe ON" %channel)

    def channelOff(self,channel):
        self.inst.write(":OUTPut%d:STATe OFF" %channel)




if __name__ == "__main__":
    # Unit test
    ps = PowerSupply({"port": "COM11"})
    ps.stopAll()
    input("Press ENTER to continue")
    while True:
        ps.voltageOutput(3, 3.3, 0.1, 5.01, 1)#voltageOutput
        print('3.3v')
        time.sleep(0.5)
        ps.voltageOutput(3, 5, 0.1, 5.01, 1)#voltageOutput
        print('5v')
        time.sleep(0.5)
        ps.voltageOutput(3, 2.2, 0.1, 5.01, 1)#voltageOutput
        print('2.2v')
        time.sleep(0.5)
