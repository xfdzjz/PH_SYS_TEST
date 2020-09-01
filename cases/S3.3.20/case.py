
import time
title = "BZ导通压降"

desc = '''
relay k5, k9 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.powersupply.voltageOutput(4, 5.5, 0.1, 3.3, 1)#vh
    ctx.powersupply.voltageOutput(2, 0, 0.1, 3.3, 1)#FI
    ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])#HORNS->SRC
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("bzOnVoltDrop")
    counter = 0
    if resp == 'ready':
        if counter ==1:
            ctx.netmatrix.arrset(['00100000','00000000','00000000','00000000'])#HORNB->SRC
        counter = counter +1
        ctx.sourcemeter.applyVoltage(0.5)
        amp = ctx.sourmeter.ampTest()
        print("I_BZNS amp is %f when sourmeter is 0.5v"%amp)
        resp = ctx.tester.runCommand("next")
        if resp != 'ready':
            return False
        input("press enter to continue")
        ctx.sourcemeter.applyVoltage(10)
        amp = ctx.sourmeter.ampTest()
        print("I_BZPB amp is %f when sourmeter is 10v"%amp)
        resp = ctx.tester.runCommand("next")
        if resp != 'ready':
            return False
        input("press enter to continue")
        ctx.powersupply.voltageOutput(2, 10, 0.1, 12, 1)
        amp = ctx.sourmeter.ampTest()
        print("I_BZPS amp is %f when sourmeter is 10v"%amp)
        resp = ctx.tester.runCommand("next")
        if resp != 'ready':
            return False
        input("press enter to continue")
        ctx.powersupply.voltageOutput(2, 0.5, 0.1, 3, 1)
        amp = ctx.sourmeter.ampTest()
        print("I_BZNB amp is %f when sourmeter is 0.5v"%amp)
        resp = ctx.tester.runCommand("next")
        if resp != 'ready':
            return False
        input("press enter to continue")

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
