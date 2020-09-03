
import time
title = "ADC通道遍历4"

desc = '''
    relay k15 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00000000','00000000','00010000','00000000'])#GP10->SRC case4
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(250)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_chn3_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        print(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        print(resp)


    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
