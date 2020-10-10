from keithley2600 import Keithley2600
import time
import logging

class SourceMeter:
    def __init__(self, config):
        self.volt = Keithley2600(config["tcp_addr"])
        retry = 5
        while retry > 0:
            try:
                self.volt.connect()
                time.sleep(1)
                self.volt.smua.source.limitv  = 5.01
                self.volt.smua.source.rangev = 5
            except:
                retry -= 1
                print("init fail, retry")
                pass


    def __del__(self):
        self.volt.disconnect()

    def stopAll(self):
        # 复位到待接线状态
        self.volt.applyVoltage(self.volt.smua, 0)

    def applyVoltage(self,vol):

        if float(vol) <= 5.0:
            self.volt.smua.source.limitv  = 5
            self.volt.smua.source.rangev = 5
            retry = 3
            while retry > 0:
                try:
                    self.volt.applyVoltage(self.volt.smua, vol)
                    break
                except:
                    retry = retry -1
                    print("Comm Error, retry")
                    time.sleep(1)
        else:
            raise SystemError


    def applyCurrent(self,amp):
        self.volt.applyCurrent(self.volt.smua, amp)


    def rampvol(self,start,target,step,de):# supply ramp voltage
        self.volt.smua.trigger.source.action = self.volt.smua.ENABLE
        self.volt.smua.trigger.measure.action = self.volt.smua.DISABLE
        self.volt.rampToVoltage(self.volt.smua, start , target,  de , step)

    def pulseTest(self,start,delay,target):
        self.volt.applyVoltage(self.volt.smua, 0)
        self.volt.applyVoltage(self.volt.smua, start)
        time.sleep(delay)
        self.volt.applyVoltage(self.volt.smua, target)

    def volTest(self):
        vol = self.volt.smua.measure.v()
        return vol

    def readbit(self,N):
        print(self.volt.digio.write(N,0))

        self.volt.digio.trigger[N].overrun= True
        self.volt.digio.trigger[N].stimulus = 4
        self.volt.digio.trigger[N].pulsewidth =0.0001
        self.volt.digio.trigger[N].mode=2
        while self.volt.digio.trigger[N].wait(1) != True:
            print("wait")

        return "ok"
    def ampTest(self):
        amp = self.volt.smua.measure.i()
        return amp

    def pulseAmp(self, start, target,targetDelay): # supply one pulse ampere
        #self.volt.smua.source.outputenableaction = 0
        #self.volt.digio.trigger[digioPin].overrun= True
        #self.volt.digio.trigger[digioPin].stimulus = 4
        #self.volt.digio.trigger[digioPin].pulsewidth = 0.0001
        #self.volt.digio.trigger[digioPin].mode=2
        #if self.volt.digio.trigger[digio_pin].wait(1) == True:
        self.volt.smua.trigger.source.listi({start,target})
        self.volt.smua.trigger.source.action = self.volt.smua.ENABLE
        self.volt.smua.trigger.measure.action = self.volt.smua.DISABLE
        self.volt.smua.trigger.source.limiti = 0.1
        self.volt.smua.source.rangev = 5
        self.volt.trigger.timer[2].clear()
        self.volt.trigger.timer[2].delay = targetDelay
        self.volt.trigger.timer[2].count = 2
        self.volt.trigger.timer[2].passthrough = True
        self.volt.trigger.timer[2].stimulus = self.volt.smua.trigger.SOURCE_COMPLETE_EVENT_ID
        self.volt.smua.trigger.source.stimulus = 0
        self.volt.smua.trigger.endpulse.action = self.volt.smua.SOURCE_HOLD
        self.volt.smua.trigger.endpulse.stimulus = self.volt.trigger.timer[2].EVENT_ID
        self.volt.smua.trigger.count = 2
        self.volt.smua.trigger.arm.count = 2
        self.volt.smua.source.output = self.volt.smua.OUTPUT_ON
        self.volt.smua.trigger.initiate()
        self.volt.waitcomplete()

        print("done")
        #else:
            #print("there is no pulse")
    def channel(self,on):
        if on == 'on':
            self.volt.smua.source.output = self.volt.smua.OUTPUT_ON
        elif on == 'off':
            self.volt.smua.source.output = self.volt.smua.OUTPUT_OFF

if __name__ == "__main__":
    print(Keithley2600.__name__)
    logger = logging.getLogger(Keithley2600.__name__)
    logger.setLevel(logging.DEBUG)  # Log等级总开关
    # Unit test
    # m = SourceMeter({"tcp_addr":"TCPIP0::172.16.60.100::INSTR"})
    m = SourceMeter({"tcp_addr":"ASRL7::INSTR"})
    for j in range(0,10):
        for i in range(0,1000):
            print("Output 3.3V %d times" %(i+j*1000))
            m.applyVoltage(3.3+ (i+j*1000)/10000)
        m.volt.disconnect()
        time.sleep(1)
        m.volt.connect()
    #m.rampvol(0,10,1,1)
    #m.pulse_amp(0.1,0.5,20,4)
    print("PASS")
