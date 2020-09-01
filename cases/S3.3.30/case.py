
import time
title = "LEDDRV电流值"

desc = '''
relay k13,k17 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#BLED->SRC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.powersupply.voltageOutput(4, 5.7, 0.1, 7, 1)#vh
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("ledDrive")
    counter = 0
    if resp == 'ready':
        if counter ==1:
            ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#BLED->SRC
        counter = counter+1
        ctx.sourcemeter.applyVoltage(2)
        amp = ctx.sourmeter.ampTest()
        print("Ibled amp is %f when VCC is 3v"%amp)
        resp = ctx.tester.runCommand("next")
        if resp != 'ready':
            return False
        input("press enter to continue")
        amp = ctx.sourmeter.ampTest()
        print("Ibled amp is %f when VCC is 3v"%amp)
        input("press enter to continue")

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
