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
    ctx.oscilloscope.trig(1,"POS",0.4)
    resp = ctx.tester.runCommand("test_dcdc_volt_5p5_volt_trim")
    while resp !='end':
        if resp == "ready1":
            vol = ctx.powersupply.measure(2, "VOLTage")
            if vol >  5.2 and vol < 5.25:
                print ("VH output voltage pass %f" %vol)
            else:
                print ("VH output voltage is %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready2":
            vol = ctx.powersupply.measure(2, "VOLTage")
            if vol >  5.75 and vol < 5.8:
                print ("VH output voltage pass %f" %vol)
            else:
                print ("VH output voltage is %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready3":
            vol = ctx.powersupply.measure(2, "VOLTage")
            if vol >  6.025 and vol < 6.0525:
                print ("VH output voltage pass %f" %vol)
            else:
                print ("VH output voltage is %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready4":
            resp = ctx.tester.runCommand("next")



    return True
