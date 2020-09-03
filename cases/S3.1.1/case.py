
import time
title = "上电后功耗"

desc = '''
relay k25 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])#VCC->SRC
    ctx.sourmeter.applyVoltage(3.3)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("TestRunPower")
    if resp == 'ready':
        amp = ctx.sourmeter.ampTest()
        print("I_VCC amp is %f when VCC is 3v"%amp)
        ctx.sourmeter.applyVoltage(4)
        amp = ctx.sourmeter.ampTest()
        print("I_VCC amp is %f when VCC is 5v"%amp)
        ctx.sourmeter.applyVoltage(2.2)
        amp = ctx.sourmeter.ampTest()
        print("I_VCC amp is %f when VCC is 2.2v"%amp)

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
