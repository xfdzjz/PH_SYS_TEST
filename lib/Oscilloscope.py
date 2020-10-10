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
        self.inst.write(":CLEar")


    def ind(self):
        self.inst.write(":RUN")

    def __del__(self):
        self.inst.close()


    def statusCheck(self): #check the status is stop or run or wait
        time.sleep(0.5)
        resu =  self.inst.query(":TRIGger:STATus?")
        print(resu)
        if resu[:4] == 'STOP':
            return True
        else:
            return False

    def staReco(self):
        self.inst.write(":RUN ")

    def stopAll(self):# reset trigger level
        # 复位到待接线状态
        self.inst.write(":TRIGger:EDGe:LEVel 0")
        self.inst.write(":TRIGger:EDGe:SLOPe RFALl")
        self.inst.write(":STOP")
        pass

    def runsta(self):
        self.inst.write(":RUN ")

    def trig(self, channel,triSlope,triVol,scale= 0.001,vscale = 1):#set trigger model
        self.inst.write(":SINGle")
        self.inst.write(":TRIGger:MODE EDGe")
        self.inst.write(":TRIGger:EDGe:SOURce CHANnel%d" %channel)
        self.inst.write(":TRIGger:EDGe:SLOPe %s" %triSlope)
        self.inst.write(":TRIGger:EDGe:LEVel %f" %triVol)
        self.inst.write(":TIMebase:MAIN:SCALe %f" %scale)
        self.inst.write(":CHANnel%d:SCALe %f "%(channel,vscale))


    def trigMul(self, channel,triSlope,triVol,scale =  0.001,vscale = 1):#set trigger model
        self.inst.write(":RUN")
        self.inst.write(":TRIGger:MODE EDGe")
        self.inst.write(":TRIGger:EDGe:SOURce CHANnel%d" %channel)
        self.inst.write(":TRIGger:EDGe:SLOPe %s" %triSlope)
        self.inst.write(":TRIGger:EDGe:LEVel %f" %triVol)
        self.inst.write(":TIMebase:MAIN:SCALe %f" %scale)
        self.inst.write(":CHANnel%d:SCALe %f "%(channel,vscale))

    def trigSlope(self, channel, PGReater,time,triVol,scale = 0.5,vscale=1):#set trigger model
        self.inst.write(":RUN")
        self.inst.write(":TRIGger:SLOPe:SOURce CHANnel%d" %channel)
        self.inst.write(":TRIGger:SLOPe:WHEN %s" %PGReater)#PGReater
        self.inst.write(":TRIGger:SLOPE:TIME %f" %time)
        self.inst.write(":TRIGger:SLOPe:ALEVel %f" %triVol)
        self.inst.write(":REFerence%d:SAVe" %channel)
        self.inst.write(":TIMebase:MAIN:SCALe %f" %scale)#time scale
        self.inst.write(":CHANnel%d:SCALe  %f "%(channel,vscale))#vertical scale like 2 means 2v

    def trigPluse(self, channel, PGReater,width,time,triVol,scale = 0.5,vscale=1):#set trigger model
        self.inst.write(":RUN")
        self.inst.write(":TRIGger:PULSe:SOURce CHANnel%d" %channel)
        self.inst.write(":TRIGger:PULSe:WHEN %s" %PGReater)#PGReater
        self.inst.write(":TRIGger:PULSe:TIME %f" %time)
        self.inst.write(":TRIGger:PULSe:WIDTh  %f" %width)
        self.inst.write(":TRIGger:PULSe:LEVel %f" %triVol)
        self.inst.write(":REFerence%d:SAVe" %channel)
        self.inst.write(":TIMebase:MAIN:SCALe %f" %scale)#time scale
        self.inst.write(":CHANnel%d:SCALe  %f "%(channel,vscale))#vertical scale like 2 means 2v




    def prepareChannel(self, channel, hz, count):  # vol_test_one
        inputChannel = ":WAVeform:SOURce CHANnel"+str(channel)
        channelOn = ":CHANnel" + str(channel) + ":DISPlay ON "
        channelCoupling = ":CHANnel" + str(channel) + ":COUPling DC"
        self.inst.write(inputChannel)
        self.inst.write(channelOn)

        self.inst.write(channelCoupling)
        self.inst.write(":WAVeform:MODE RAW")
        self.inst.write(":WAVeform:POINts %d" % (count))
        self.inst.write(":SOURce:FREQuency %dHz" % (hz))
        self.inst.write(":WAVeform:FORMat ASCii")
        #preambleString = self.inst.query(":WAVeform:PREamble?")
        #format = self.inst.query(":WAVeform:FORMat?")

    def getWave(self, channel, hz, count):  # vol_test_one
        self.inst.write(":WAVeform:DATA?")
        data = self.inst.read_raw()
        val = data.decode().split(",")
        val[0] = val[0][11:]

        for i in range(0,len(val)-1):
            val[i] = float(val[i])

        print("read_data length is %d" %len(val))
        return (val)

    def readRamData(self,channel,count,start,final, do ='false'):
        data = []
        j=0
        self.inst.write(":STOP")
        self.inst.write("WAV:SOUR CHAN%d" %channel)
        self.inst.write(":WAV:MODE NORMal")
        self.inst.write(":WAV:FORM ASCii")
        #ramSpace= final//count
        self.inst.write(":WAV:STAR %d" %start)
        self.inst.write(":WAV:STOP  %d" %final)
        data = self.inst.query(":WAV:DATA?")
        val = data.split(",")
        val[0] = val[0][11:]
        val[len(val)-1] = val[len(val)-1] [:-1]
        print(len(val))
        if do == 'false':
            for i in range(0,len(val)):
                val[i] = float(val[i])
                #val[i] = round(val[i])val,
            while val[j] <= 3:
                j=j+1

            return val,j
        else:
            return val
                #print("val is greater than 0.5 in number %d, val is %f"%(i,val[i]))
        #for i in range(1,final,ramSpace):
        #    print("wave data are ")
        #    print(val[(i-1):i+ramSpace-1])



    def volTest(self, channel):
        vol = []
        self.inst.write(":MOD ON")
        self.inst.write(":RUN")
        self.inst.write(":MEASure:ADISplay ON")
        self.inst.write(":MEASure:SSOURce CHANnel%d" %channel)
        self.inst.write(":MEASure:ITEM PDUTy,CHANnel%d"%channel)
        #self.inst.write(":MEASure:STATistic:DISPlay ON")
        base = self.inst.query(":MEASure:ITEM? VBASe,CHANnel%d" % channel)
        avg = self.inst.query(":MEASure:ITEM? VAVG,CHANnel%d" % channel)
        top = self.inst.query(":MEASure:ITEM? VTOP,CHANnel%d" % channel)
        min = self.inst.query(":MEASure:ITEM? VMIN,CHANnel%d" % channel)
        vpp = self.inst.query(":MEASure:ITEM? VPP,CHANnel%d" % channel)
        vol.append(base)
        vol.append(avg)
        vol.append(top)
        vol.append(min)
        vol.append(vpp)

        return vol


    def paraTest(self,channel):
        para = []

        # self.inst.write(":MEASure:CLEar ALL")
        # self.inst.write(":RUN")
        # self.inst.write(":MEASure:ADISplay ON")
        # self.inst.write(":MEASure:SSOURce CHANnel%d" %channel)
        # self.inst.write(":MEASure:ITEM PDUTy,CHANnel%d"%channel)
        # time.sleep(1)
        # duty = self.inst.query(":MEASure:ITEM? PDUTy,CHANnel%d"%channel)
        # time.sleep(1)
        # self.inst.write(":MEASure:CLEar ALL")
        # self.inst.write(":MEASure:ITEM FREQuency,CHANnel%d"%channel)
        # time.sleep(1)
        # frequency = self.inst.query(":MEASure:ITEM? FREQuency,CHANnel%d"%channel)
        # print(duty)
        # print(frequency)
        # para.append(float(duty))
        # para.append(float(frequency))
        # self.inst.write(":MEASure:ADISplay OFF")
        # #self.inst.write(":MOD OFF")
        # self.inst.write(":STOP")
        self.inst.write(":MEASure:CLEar ALL")
        self.inst.write(":RUN")
        self.inst.write(":MEASure:SSOURce CHANnel%d" %channel)
        self.inst.write(":MEASure:ITEM PDUTy,CHANnel%d"%channel)
        self.inst.write(":MEASure:ITEM FREQuency,CHANnel%d"%channel)
        self.inst.write(":MEASure:ADISplay ON")
        time.sleep(0.3)
        self.inst.write(":MEASure:ADISplay OFF")
        duty = self.inst.query(":MEASure:ITEM? PDUTy,CHANnel%d"%channel)
        frequency = self.inst.query(":MEASure:ITEM? FREQuency,CHANnel%d"%channel)
        self.inst.write(":STOP")
        para.append(float(duty))
        para.append(float(frequency))
        return para

    def xincre(self):
        return self.inst.query (":WAVeform:XINCrement? ")


    def getVoltage(self, channel):
        # TODO: calc a mean value here
        pass

if __name__ == "__main__":
    # Unit test
    osc = Oscilloscope({"tcp_addr":"TCPIP::172.16.60.164::inst0::INSTR"})
    #m = SourceMeter({"tcp_addr":"TCPIP0::172.16.60.100::INSTR"})
    input("Press ENTER to continue")
    print("trigger")
    #osc.trig(3,2,"NEGative")
    #m.pulseTest(3,0.1,1)
    input("Press ENTER to continue")
    #print("Get 300@1000Hz from channel #3")
    osc.prepareChannel(3, 1000, 300)
    ret = osc.getWave(3, 1000, 300)
    print(ret)
    print(max(ret))
    #print("Get 3000@10000Hz from channel #3")
    #input("Press ENTER to continue")
    #ret = osc.getWave(3, 10000, 1025)
    #print(ret)
    #print(len(ret))
    print("PASS")
