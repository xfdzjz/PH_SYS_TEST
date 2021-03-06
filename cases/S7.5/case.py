import time
import numpy as np
title = "8V纹波、带载"

desc = '''
    relay k4,k15 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
        '''

    vol = 3

    # 芯片上电VCC=3V

    ctx.netmatrix.arrset(['00000000','00000000','00010000','10000000'])#GP00 ->osc1 gp14->osc2
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 4, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_volt_8p0wave")
    while resp != 'end':
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp == 'ready':
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,7,0.001,5)
            ctx.oscilloscope.trig(2,"POS",1,0.001,1)
            ctx.oscilloscope.trig(4,"POS",1,0.001,1)
            #ctx.oscilloscope.trig(1,"POS",1,0.001,1)


            ctx.oscilloscope.prepareChannel(4, 30000, 15625)
            ctx.oscilloscope.prepareChannel(2, 30000, 15625)
            ctx.oscilloscope.prepareChannel(3, 30000, 15625)

            time.sleep(3.2)
            resp = ctx.tester.runCommand("next")
            #ctx.sourcemeter.rampvol(0,4,1,0.01)


            #time.sleep(5)#示波器配置等的时8s间

            #ctx.powersupply.voltageOutput(2, 0, 0.1, 3, 1)#channel, V, I, ovp, ocp
            #time.sleep(1)
            #ctx.powersupply.voltageOutput(2, 2, 0.1, 3, 1)
            #time.sleep(1)
            #ctx.powersupply.voltageOutput(2, 0, 0.1, 3, 1)
            #time.sleep(1)
            #ctx.sourcemeter.rampvol(0,5,1,0.5)
            ctx.logger.info("channel4")
            GP14,count14 = ctx.oscilloscope.readRamData(4,2,1,15625)
            ctx.logger.info("channel2")
            GP00,count00 = ctx.oscilloscope.readRamData(2,2,1,15625)
            ctx.logger.info("channel3")
            VH,test = ctx.oscilloscope.readRamData(3,2,1,15625)
            ctx.logger.info(VH[len(VH)-5])
            for i in range(0,len(VH)-1):
                if VH[i] >= 7.2:
                    ctx.logger.info(VH[i])
                    ctx.logger.debug(VH[i])
                    Tset =1/30*i
                    ctx.logger.info("Tset is %f ms"%Tset )
                    ctx.logger.debug("Tset is %f ms"%Tset )
                break

            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            ctx.logger.info("VPP is %fv" %VPPVH)
            ctx.logger.debug("VPP is %fv" %VPPVH)
            ctx.logger.info ("VH vol is %f or %f" %(VH[count14],VH[count00]))
            ctx.logger.debug ("VH vol is %f or %f" %(VH[count14],VH[count00]))

            #ctx.sourcemeter.applyVoltage(1.6)
            ctx.powersupply.channelOn(1)
            ctx.powersupply.resistor(1,160,5,0.1)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,3.3,0.001,5)
            VH,test = ctx.oscilloscope.readRamData(3,2,1,15625)
            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            ctx.logger.info("VPP is %fv" %VPPVH)
            ctx.logger.debug("VPP is %fv" %VPPVH)

            ctx.powersupply.channelOn(1)
            ctx.powersupply.resistor(1,80,5,0.5)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,3.3,0.001,5)
            VH,test = ctx.oscilloscope.readRamData(3,2,1,15625)
            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            ctx.logger.info("VPP is %fv" %VPPVH)
            ctx.logger.debug("VPP is %fv" %VPPVH)
            ctx.powersupply.channelOff(1)




    return True
