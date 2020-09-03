import time
title = "10V纹波、带载"

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
    ctx.powersupply.voltageOutput(1, 3.3, 0.1, 4, 1)
    time.sleep(250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.oscilloscope.trig(1,'POS',0.4)
    resp = ctx.tester.runCommand("test_dcdc_volt_10p0wave")
    while resp !='end':
        if resp == "ready":
            while ctx.oscilloscope.statusCheck() != True:
                start = time.time()
            ctx.oscilloscope.prepareChannel(1, 1000, 5000)
            GP00 = ctx.oscilloscope.getWave(1, 1000, 5000)
            ctx.oscilloscope.trig(2,'POS',0.4)
            while ctx.oscilloscope.statusCheck() != True:
                end = time.time()
            ctx.oscilloscope.prepareChannel(2, 1000, 5000)
            GPI4 = ctx.oscilloscope.getWave(2, 1000, 5000)
            ctx.oscilloscope.trigSlope(3,"PGReater",0.4,8)
            while ctx.oscilloscope.statusCheck() != True:
                final = time.time()
            ctx.oscilloscope.prepareChannel(3, 1000, 10000)
            VH = ctx.oscilloscope.getWave(3, 1000, 10000)
            print("VH vol is %f"% VH[len(VH)-1])
            print ("time intv is %f" %(final-start))

            ctx.oscilloscope.prepareChannel(3, 1000, 10000)
            VH = ctx.oscilloscope.getWave(3, 1000, 10000)
            print("VH vol is %f"% VH[len(VH)-1])

            ctx.oscilloscope.prepareChannel(3, 1000, 10000)
            VH = ctx.oscilloscope.getWave(3, 1000, 10000)
            print("VH vol is %f"% VH[len(VH)-1])
            resp = ctx.tester.runCommand("next")




    return True
