import time
import numpy as np
title = "DCDC VOOK功能"

desc = '''
    源表 <=> PDAS
    稳压源channel2 <=> VCC
    示波器 <=> GP15(VO1)
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
        '''

    vol = 3

    # 芯片上电VCC=3V
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 4, 1)
    ctx.netmatrix.arrset(['10000000','01000000','00100000','00010000'])
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_volt_8p0wave")
    while resp != 'end':
        print(resp)
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
            print("channel4")
            GP14,count14 = ctx.oscilloscope.readRamData(4,2,1,15625)
            print("channel2")
            GP00,count00 = ctx.oscilloscope.readRamData(2,2,1,15625)
            print("channel3")
            VH,test = ctx.oscilloscope.readRamData(3,2,1,15625)
            print(VH[len(VH)-5])
            for i in range(0,len(VH)-1):
                if VH[i] >= 7.2:
                    print(VH[i])
                    Tset =1/30*i
                    print("Tset is %f ms"%Tset )
                break

            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            print("VPP is %fv" %VPPVH)

            print ("VH vol is %f or %f" %(VH[count14],VH[count00]))
            input("press enter to continue test to lod 16ohm")

            #ctx.sourcemeter.applyVoltage(1.6)
            ctx.powersupply.channelOn(1)
            ctx.powersupply.resistor(1,160,5,0.1)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,3.3,0.001,5)
            VH,test = ctx.oscilloscope.readRamData(3,2,1,15625)
            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            print("VPP is %fv" %VPPVH)
            input("press enter to continue test to lod 32ohm")

            ctx.powersupply.channelOn(1)
            ctx.powersupply.resistor(1,80,5,0.5)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.0001,3.3,0.001,5)
            VH,test = ctx.oscilloscope.readRamData(3,2,1,15625)
            VPP = []
            vmin = len(VH)//3*2
            VPP = VH[vmin:len(VH)-1]
            VPPVH = max(VPP)-min(VPP)
            print("VPP is %fv" %VPPVH)
            input("press enter to end case")
            ctx.powersupply.channelOff(1)




    return True