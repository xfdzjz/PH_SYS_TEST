
import time
title = "indLed导通压降"

desc = '''
relay k1 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['10000000','00000000','00000000','00000000'])#GP15->src
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(250)
    ctx.sourmeter.applyVoltage(3.3-0.5)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("indLedOnVoltDrop")
    if resp == 'ready':
        amp = ctx.sourmeter.ampTest()
        print("indled amp is %f when VCC is 3v"%amp)
        input("press enter to continue")
        ctx.powersupply.voltageOutput(3, 5, 0.1, 3.3, 1)
        amp = ctx.sourmeter.ampTest()
        print("indled amp is %f when VCC is 5v"%amp)
        input("press enter to continue")
        ctx.powersupply.voltageOutput(3, 2.2, 0.1, 3.3, 1)
        amp = ctx.sourmeter.ampTest()
        print("indled amp is %f when VCC is 2.2v"%amp)

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
