import time
import logging
import serial
import numpy as np

script = '''
loadscript TSB_Script
function amp_pre()
	 smua.source.autorangei = smua.AUTORANGE_ON
	 smua.source.autorangev = smua.AUTORANGE_ON
	 smua.trigger.source.listi({100E-9})
	 smua.trigger.source.action = smua.ENABLE
	 smua.trigger.measure.action = smua.DISABLE
	 trigger.timer[2].clear()
	 trigger.timer[2].delay = 0.0001
	 trigger.timer[2].count = 2
	 trigger.timer[2].passthrough = true
	 trigger.timer[2].stimulus = smua.trigger.SOURCE_COMPLETE_EVENT_ID
	 smua.trigger.source.stimulus = 0
	 smua.trigger.endpulse.action = smua.SOURCE_HOLD
	 smua.trigger.endpulse.stimulus = trigger.timer[2].EVENT_ID
	 smua.trigger.count = 2
	 smua.trigger.arm.count = 2
	 smua.source.output = smua.OUTPUT_ON
end

function amp()
	 amp_pre()
	 digio.trigger[4].mode = digio.TRIG_FALLING
	 digio.trigger[4].clear()
     display.clear()
     display.settext("WAIT...")
	 local triggered = digio.trigger[4].wait(2)
	 if triggered then
        display.settext("OK")
	 	smua.trigger.initiate()
		waitcomplete()
     else
	 	display.settext("NO")
	 end
	 digio.trigger[4].release()
	 digio.trigger[4].reset()
end

amp()
endscript
'''


class SourceMeter:
    def __init__(self, config):
        self.port = serial.Serial(config["port"], config["baudRate"],timeout=2)


    def __del__(self):
        try:
            self.port.close()
        except:
            pass

    def stopAll(self):
        # 复位到待接线状态
        self.runCommand('smua.source.levelv = 0')
        self.runCommand('smua.source.output = smua.OUTPUT_OFF')
        self.runCommand('display.smua.measure.func = display.MEASURE_DCVOLTS')
        self.runCommand('smua.source.limitv = 30')
        # self.runCommand('errorqueue.clear()')

    def runCommand(self, cmd):# communication using serial port and how much string number will be read
        self.port.write((cmd+'\r\n').encode('ascii')) # command ending char " "

    def loadScript(self):
        lines = script.split("\n")
        for line in lines:
            self.port.write((line + '\r\n').encode('ascii'))

    def readCommand(self, cmd):# communication using serial port and how much string number will be read
        self.port.write((cmd+'\r\n').encode('ascii')) # command ending char " "
        time.sleep(0.5)
        readVal = self.port.read_all()
        val = readVal.decode("ascii")
        return val


    def applyVoltage(self,vol):
        if vol <=5.0 and vol >=-1:
            self.runCommand('smua.source.func = smua.OUTPUT_DCVOLTS')
            self.runCommand('smua.source.levelv = %f' %vol)
            self.runCommand('smua.source.output = smua.OUTPUT_ON')
            self.runCommand('smua.source.limiti = 0.2')
            time.sleep(0.3) # 等待 300ms 电压正常输出
        else:
            raise SystemError


    def applyVol(self,vol):
        if vol <=10.1 and vol >=-1:
            self.runCommand('smua.source.rangev= 100')
            self.runCommand('smua.source.limitv= 10.1')
            self.runCommand('smua.source.rangei = 0.2')
            self.runCommand('smua.source.func = smua.OUTPUT_DCVOLTS')
            self.runCommand('smua.source.levelv = %f' %vol)
            self.runCommand('smua.source.output = smua.OUTPUT_ON')
        else:
            raise SystemError



    def applyCurrent(self,amp):
        self.runCommand('smua.cal.polarity = smua.CAL_POSITIVE')
        if amp <=5.0 and amp >=-1:
            self.runCommand('smua.source.func = smua.OUTPUT_DCAMPS')
            self.runCommand('smua.source.leveli = %f' %amp)
            self.runCommand('smua.source.output = smua.OUTPUT_ON')
        else:
            raise SystemError


    # def rampvol(self,start,target,step,de):# supply ramp voltage
    #     smua.trigger.source.action = smua.ENABLE
    #     smua.trigger.measure.action = smua.DISABLE
    # rampToVoltage(self.volt.smua, start , target,  de , step)

    def pulseTest(self,start,delay,target):
        self.applyVoltage( 0)
        self.applyVoltage(start)
        time.sleep(delay)
        self.applyVoltage(target)

    def volTest(self):
        self.runCommand('display.smua.measure.func = display.MEASURE_DCVOLTS')
        self.runCommand('smua.measure.autorangev = smua.AUTORANGE_ON')
        self.runCommand('smua.source.rangev = 3')
        # self.runCommand('smua.source.limitv = 3')
        self.runCommand('smua.source.output = smua.OUTPUT_ON')
        # self.runCommand('smua.source.rangei = 0.1')
        # self.runCommand('smua.source.limiti = 0.1')
        a =  float(self.readCommand('print(smua.measure.v())'))
        return a


    def ampTest(self):
        self.runCommand('display.smua.measure.func = display.MEASURE_DCAMPS')
        self.runCommand('smua.measure.autorangei = smua.AUTORANGE_ON')
        self.runCommand('smua.measure.autorangev = smua.AUTORANGE_ON')
        self.runCommand('smua.source.rangei = 0.1')
        self.runCommand('smua.source.output = smua.OUTPUT_ON')
        amp =  self.readCommand('print(smua.measure.iv())')
        for i in range(0,len(amp)):
            if amp[i]== 'e':
                # print(amp[0:i+4])
                amp = float(amp[0:i+4])
                break
        return amp

    def ivTest(self):
        self.runCommand('display.smua.measure.func = display.MEASURE_DCVOLTS')
        self.runCommand('smua.measure.autorangei = smua.AUTORANGE_ON')
        self.runCommand('smua.measure.autorangev = smua.AUTORANGE_ON')
        self.runCommand('smua.source.rangev = 3')
        self.runCommand('smua.source.rangei = 0.1')
        self.runCommand('smua.source.output = smua.OUTPUT_ON')
        s =  self.readCommand('print(smua.measure.iv())')
        [i,v] = s.split()
        return float(i),float(v)

    def channel(self,on):
        if on == 'on':
            self.runCommand('smua.source.output = smua.OUTPUT_ON')
        elif on == 'off':
            self.runCommand('smua.source.output = smua.OUTPUT_OFF')

    def pulseAmp(self, start, target,targetDelay): # supply one pulse ampere
    #self.volt.smua.source.outputenableaction = 0
    #self.volt.digio.trigger[digioPin].overrun= True
    #self.volt.digio.trigger[digioPin].stimulus = 4
    #self.volt.digio.trigger[digioPin].pulsewidth = 0.0001
    #self.volt.digio.trigger[digioPin].mode=2
    #if self.volt.digio.trigger[digio_pin].wait(1) == True:
        self.runCommand('smua.trigger.source.listi({%f,%f})' %(start,target))
        self.runCommand('smua.trigger.source.action = smua.ENABLE')
        self.runCommand('smua.trigger.measure.action = smua.DISABLE')
        self.runCommand('smua.trigger.source.limiti = 0.1')
        self.runCommand('smua.source.rangev = 5')
        self.runCommand('trigger.timer[2].clear()')
        self.runCommand('trigger.timer[2].delay = %f' %targetDelay)
        self.runCommand('trigger.timer[2].count = 2')
        self.runCommand('trigger.timer[2].passthrough = True')
        self.runCommand('trigger.timer[2].stimulus = smua.trigger.SOURCE_COMPLETE_EVENT_ID')
        self.runCommand('smua.trigger.source.stimulus = 0')
        self.runCommand('smua.trigger.endpulse.action = smua.SOURCE_HOLD')
        self.runCommand('smua.trigger.endpulse.stimulus = trigger.timer[2].EVENT_ID')
        self.runCommand('smua.trigger.count = 2')
        self.runCommand('smua.trigger.arm.count = 2')
        self.runCommand('smua.source.output = smua.OUTPUT_ON')
        self.runCommand('smua.trigger.initiate()')
        self.runCommand('waitcomplete()')


    def rampvol(self,start,target,de,steps):
        self.runCommand('smua.source.output = smua.OUTPUT_ON')
        vcurr = start
        if vcurr == target:
            return
        self.runCommand('display.smua.measure.func = display.MEASURE_DCVOLTS')
        step = np.sign(target - vcurr) * abs(steps)
        for v in np.arange(vcurr, target, step):
             self.runCommand('smua.source.levelv = %f' %v)
             time.sleep(de)
        self.runCommand('smua.source.levelv = %f' % target)
        self.runCommand('beeper.beep(0.3, 2400)')









if __name__ == "__main__":
    m = SourceMeter({"tcp_addr":"TCPIP0::172.16.60.100::INSTR","port":"COM7","baudRate": 115200})
    m.applyVoltage(3)
    print(m.ivTest())
    # m.loadScript()
    print("PASS")
