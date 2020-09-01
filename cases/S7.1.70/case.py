import time
title = "10V电压校准"

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
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.oscilloscope.trig(1,"POS",0.4)
    resp = ctx.tester.runCommand("test_dcdc_volt_10p0_volt_trim")
    while resp !='end':
        if resp == "ready1":
            vol = ctx.powersupply.measure(2, "VOLTage")
            if vol >  9.475 and vol < 9.525:
                print ("VH output voltage pass %f" %vol)
            else:
                print ("VH output voltage is %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready2":
            vol = ctx.powersupply.measure(2, "VOLTage")
            if vol >  10.475 and vol < 10.525:
                print ("VH output voltage pass %f" %vol)
            else:
                print ("VH output voltage is %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready3":
            vol = ctx.powersupply.measure(2, "VOLTage")
            if vol >  10.975 and vol < 11.025:
                print ("VH output voltage pass %f" %vol)
            else:
                print ("VH output voltage is %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready4":
            resp = ctx.tester.runCommand("next")



    return True
