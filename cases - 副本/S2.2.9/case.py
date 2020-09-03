
import time
title = "ISRCA 5uA电流"

desc = '''
relay k17 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP15->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("ISRCA5uA")
    if resp == 'ready':
        vol = ctx.sourcemeter.volTest()
        print("Visrca vol is %f"%vol)

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
