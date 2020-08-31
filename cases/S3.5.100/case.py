
import time
title = "VDD稳定性测试"

desc = '''
    在时钟trim后做此项测试
    稳压源 Channel3 <=> VCC
    源表  <=> VBGS
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP08->SRC case5
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_chn9_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        print(resp)
        input("press enter to continue")
        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        print(resp)
        input("press enter to continue")

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
