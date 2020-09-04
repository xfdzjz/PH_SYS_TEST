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
    ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])#GP04->src

    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_ref_sel")
    if resp != 'ready':
        return False

    ctx.sourcemeter.applyVoltage(0.5)
    resp = ctx.tester.runCommand("next")
    print(resp)
    ctx.sourcemeter.applyVoltage(1.5)
    resp = ctx.tester.runCommand("next")
    print(resp)

    ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])##GP04->src,GP14->vref
    ctx.powersupply.voltageOutput(4, 2.5, 0.1, 5, 1)

    ctx.sourcemeter.applyVoltage(0.5)
    resp = ctx.tester.runCommand("next")
    print(resp)
    ctx.sourcemeter.applyVoltage(1.5)
    resp = ctx.tester.runCommand("next")
    print(resp)

    resp = ctx.tester.runCommand("next")
    if resp != 'end':
        return False
    return True
