
import time
title = "V1P5D带载能力"

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
    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP15->src
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_v1p5d_load")


    while resp !='end':
        print(resp)
        if resp == 'ready':
            vol = ctx.sourcemeter.volTest()
            print("VCC is 3.3v vol is %f" %vol)
            input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            vol = ctx.sourcemeter.volTest()
            print("VCC is 5v vol is %f" %vol)
            input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            vol = ctx.sourcemeter.volTest()
            print("VCC is 2.2v vol is %f" %vol)
            input("press enter to continue case")
            resp = ctx.tester.runCommand("next")
        else:
            return False
    return True
