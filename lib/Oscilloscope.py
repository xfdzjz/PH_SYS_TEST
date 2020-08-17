import visa
import string
import struct
import time
from lib.SourceMeter import SourceMeter

wav_form_dict = {
    0: "BYTE",
    1: "WORD",
    4: "ASCii",
}
acq_type_dict = {
    0: "NORMal",
    1: "PEAK",
    2: "AVERage",
    3: "HRESolution",
}


class Oscilloscope:
    def __init__(self, config):
        rm = visa.ResourceManager()
        inst = rm.open_resource(config["tcp_addr"])
        self.inst = inst

    def __del__(self):
        self.inst.close()
        pass

    def statusCheck(self):  # check the status is stop or run or wait
        time.sleep(0.5)
        resu = self.inst.query(":TRIGger:STATus?")
        print(resu)
        if resu[:4] == 'STOP':
            return True
        else:
            return False

    def stopAll(self):  # reset trigger level
        # 复位到待接线状态
        self.inst.write(":TRIGger:EDGe:LEVel 0")
        self.inst.write(":TRIGger:EDGe:SLOPe RFALl")
        self.inst.write(":STOP")
        pass

    def trig(self, channel, triVol, triSlope):  # set trigger model
        self.inst.write(":SINGle")
        self.inst.write(":TRIGger:EDGe:SOURce CHANnel%d" % channel)
        self.inst.write(":TRIGger:EDGe:SLOPe %s" % triSlope)
        self.inst.write(":TRIGger:EDGe:LEVel %d" % triVol)

    def prepareChannel(self, channel, hz, count):  # vol_test_one
        inputChannel = ":WAVeform:SOURce CHANnel"+str(channel)
        channelOn = ":CHANnel" + str(channel) + ":DISPlay ON "
        channelOffset = ":CHANnel" + str(channel) + ":OFFSet 0"
        channelInvert = ":CHANnel" + str(channel) + ":INVert OFF"
        channelCoupling = ":CHANnel" + str(channel) + ":COUPling DC"
        self.inst.write(inputChannel)
        self.inst.write(channelOn)
        self.inst.write(channelOffset)
        self.inst.write(channelCoupling)
        self.inst.write(channelInvert)
        self.inst.write(":WAVeform:POINts %d" % (count))
        self.inst.write(":SOURce:FREQuency %dHz" % (hz))
        self.inst.write(":WAVeform:FORMat ASCii")
        preambleString = self.inst.query(":WAVeform:PREamble?")
        format = self.inst.query(":WAVeform:FORMat?")
        # FIXME: leading #900000XXXX shall be removed
        # FIXME: convert return value to float here

    def getWave(self, channel, hz, count):  # vol_test_one
        # input_channel = ":WAVeform:SOURce CHANnel"+str(channel)
        # channel_on = ":CHANnel" + str(channel) + ":DISPlay ON "
        # channel_offset = ":CHANnel" + str(channel) + ":OFFSet 0"
        # channel_invert = ":CHANnel" + str(channel) + ":INVert OFF"
        # channel_coupling = ":CHANnel" + str(channel) + ":COUPling DC"
        # self.inst.write(input_channel)
        # self.inst.write(channel_on)
        # self.inst.write(channel_offset)
        # self.inst.write(channel_coupling)
        # self.inst.write(channel_invert)
        # self.inst.write(":WAVeform:POINts %d" % (count))
        # self.inst.write(":SOURce:FREQuency %dHz" % (hz))
        # self.inst.write(":WAVeform:FORMat ASCii")
        # preamble_string = self.inst.query(":WAVeform:PREamble?")
        # format = self.inst.query(":WAVeform:FORMat?")
        self.inst.write(":WAVeform:DATA?")
        data = self.inst.read_raw()

        val = data.decode().split(",")
        val[0] = val[0][11:]
        for i in range(0, len(val)):
            val[i] = float(val[i])
        print(val)
        return (val)

    def getVoltage(self, channel):
        # TODO: calc a mean value here
        pass


if __name__ == "__main__":
    # Unit test
    osc = Oscilloscope({"tcp_addr": "TCPIP::172.16.60.164::inst0::INSTR"})
    m = SourceMeter({"tcp_addr": "TCPIP0::172.16.60.100::INSTR"})
    input("Press ENTER to continue")
    print("trigger")
    osc.trig(3, 2, "NEGative")
    m.pulseTest(3, 0.1, 1)
    input("Press ENTER to continue")
    # print("Get 300@1000Hz from channel #3")
    ret = osc.prepareChannel(3, 1000, 300)
    ret = osc.getWave(3, 1000, 300)
    # print(ret)
    # print(len(ret))
    # print("Get 3000@10000Hz from channel #3")
    #input("Press ENTER to continue")
    #ret = osc.getWave(3, 10000, 1025)
    # print(ret)
    # print(len(ret))
    print("PASS")
