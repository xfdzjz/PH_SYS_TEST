
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
    ctx.sourmeter.applyVoltage(3.3)
    ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])#VCC->SRC
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("DeepSleep")
    if resp == 'ready':
        amp = ctx.sourmeter.ampTest()
        print("I_dsleep amp is %f when VCC is 3v"%amp)
        input("press enter to continue")
        ctx.sourmeter.applyVoltage(5)
        amp = ctx.sourmeter.ampTest()
        print("I_dsleep amp is %f when VCC is 5v"%amp)
        input("press enter to continue")
        ctx.sourmeter.applyVoltage(2.2)
        amp = ctx.sourmeter.ampTest()
        print("I_dsleep amp is %f when VCC is 2.2v"%amp)

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
