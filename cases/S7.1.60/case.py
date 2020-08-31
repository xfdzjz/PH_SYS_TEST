import time
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
    ctx.powersupply.voltageOutput(1, 3.3, 0.1, 4, 1)
    ctx.netmatrix.arrset(['10000000','01000000','00100000','00010000'])
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.oscilloscope.trig(1,POS,0.4)
    resp = ctx.tester.runCommand("test_dcdc_volt_10p0wave")
    while resp !='end':
        if resp == "ready":
            while statusCheck() != True:
                start = time.time()
            ctx.oscilloscope.prepareChannel(1, 1000, 5000)
            GP00 = ctx.oscilloscope.getWave(1, 1000, 5000)
            ctx.oscilloscope.trig(2,POS,0.4)
            while statusCheck() != True:
                end = time.time()
            ctx.oscilloscope.prepareChannel(2, 1000, 5000)
            GPI4 = ctx.oscilloscope.getWave(2, 1000, 5000)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.4,8)
            while statusCheck() != True:
                final = time.time()
            ctx.oscilloscope.prepareChannel(3, 1000, 10000)
            VH = ctx.oscilloscope.getWave(3, 1000, 10000)
            print("VH vol is %f"% VH[len(VH)-1])
            print ("time intv is %f" %(final-start))
            input("press enter to continue case to change load")
            ctx.oscilloscope.prepareChannel(3, 1000, 10000)
            VH = ctx.oscilloscope.getWave(3, 1000, 10000)
            print("VH vol is %f"% VH[len(VH)-1])
            input("press enter to continue case to change load")
            ctx.oscilloscope.prepareChannel(3, 1000, 10000)
            VH = ctx.oscilloscope.getWave(3, 1000, 10000)
            print("VH vol is %f"% VH[len(VH)-1])
            resp = ctx.tester.runCommand("next")




    return True
