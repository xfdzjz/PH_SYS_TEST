
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
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.netmatrix.arrset(['00000000','00000000','00000000','00010000'])#GP14->sourmeter
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("VBGSTestOnVCCVerify")

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
        else:
            return False
        resp = ctx.tester.runCommand("next")

    return True
