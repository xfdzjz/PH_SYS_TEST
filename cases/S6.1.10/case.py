import time
title = "DCDC占空比"

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

    # 芯片上电VCC=3V
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    ctx.netmatrix.arrset(['00000000','00000000','00100000','01000000'])
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_duty")


    while resp != 'end':
        if resp == 'ready':
            ctx.sourcemeter.applyCurrent(2e-6)
            ctx.oscilloscope.prepareChannel(3, 1000, 300)
            wave = ctx.oscilloscope.getWave(3, 1000, 300)
            para = ctx.oscilloscope.paraTest(3)
            duty = 100*float(para[0])
            freq = float(para[1])


            print("duty is %f percent, frequency is %f"%(duty,freq))
            print(wave)
            resp = ctx.tester.runCommand("next")
        else:
            return False



    return True
