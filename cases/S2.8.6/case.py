import time
title = "LVD检测"

desc = '''
    源表 <=> GP19
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''

    # 芯片上电VCC=3V
    ctx.sourcemeter.applyVoltage(3.3)
    ctx.netmatrix.arrset(['00000000','00010000','00000000','01000000'])#GP04->OSC GP14->vref
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_mult_samp")

    input("input is 1.5v press ENTER to continue")

    ctx.powersupply.voltageOutput(1, 1.5, 0.1, 5, 1)

    resp = ctx.tester.runCommand("next")
    print("final result is %s" %resp)

    return True
