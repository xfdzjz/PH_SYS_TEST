import time
title = "LVD检测"

desc = '''
    relay k5,k14 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''

    # 芯片上电VCC=3V
    ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])#GP04->src GP14->vref
    ctx.sourcemeter.applyVoltage(3.3)
    time.sleep(250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_mult_samp")


    ctx.powersupply.voltageOutput(1, 1.5, 0.1, 5, 1)

    resp = ctx.tester.runCommand("next")
    print("final result is %s" %resp)

    return True
