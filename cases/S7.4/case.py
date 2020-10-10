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
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_dcdc_volt_8p0wave")
    while resp != 'end':
        ctx.logger.info(resp)
        if resp == 'ready':
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,3.3,0.001,5)
            #ctx.oscilloscope.trigMul(2,"POS",1,0.001,1)
            #ctx.oscilloscope.trigMul(4,"POS",1,0.001,1)

            ctx.oscilloscope.prepareChannel(4, 30000, 15625)
            ctx.oscilloscope.prepareChannel(2, 30000, 15625)
            ctx.oscilloscope.prepareChannel(3, 30000, 15625)

            time.sleep(3.2)
            resp = ctx.tester.runCommand("next")

            ctx.powersupply.voltageOutput(1, 3, 0.1, 5, 1)
            ctx.powersupply.voltageOutput(2, 3, 0.1, 5, 1)
            ctx.sourcemeter.rampvol(0,5,0.5,0.1)

            VH = ctx.oscilloscope.readRamData(3,2,1,15625,'true')
            GP14 = ctx.oscilloscope.readRamData(4,2,1,15625,'true')
            GP00 = ctx.oscilloscope.readRamData(2,2,1,15625,'true')

            for i in range(0,len(VH)):
                VH[i] = float(VH[i])
            for j in range(0,len(GP00)):
                GP00[j] = float(GP00[j])
            #ctx.logger.info(VH[len(VH)-5])
            for i in range(0,len(VH)):
                if VH[i] >= 4.9:
                    ctx.logger.info("VH vol is %f" %VH[i])
                    break

            for j in range(0,len(GP00)):
                if GP00[j] >= 3.0:
                    break
            timeDiff =float( ctx.oscilloscope.xincre())
            Tset = timeDiff*(np.abs(i - j))
            ctx.logger.info("Tset is %f ms"%Tset )
            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            ctx.logger.info("VPP is %fv" %VPPVH)


            ctx.powersupply.channelOn(1)
            ctx.powersupply.resistor(1,160,5,0.1)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,3.3,0.001,5)
            ctx.sourcemeter.rampvol(0,5,0.5,0.1)
            VH= ctx.oscilloscope.readRamData(3,2,1,15625,'true')
            for i in range(0,len(VH)):
                VH[i] = float(VH[i])
            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            ctx.logger.info("VPP is %fv" %VPPVH)


            ctx.powersupply.channelOn(1)
            ctx.powersupply.resistor(1,80,5,0.5)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,3.3,0.001,5)
            ctx.sourcemeter.rampvol(0,5,0.5,0.1)
            VH= ctx.oscilloscope.readRamData(3,2,1,15625,'true')
            for i in range(0,len(VH)):
                VH[i] = float(VH[i])
            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            ctx.logger.info("VPP is %fv" %VPPVH)

            ctx.powersupply.channelOff(1)

    return True
