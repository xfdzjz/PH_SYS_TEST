
import time
title = "MRC随VCC变化"

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
    ctx.netmatrix.arrset(['00000000','00010000','00000000','00000000'])#GP14->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("MRCTestOnVCCVerify")

    while resp !='end':
        print(resp)
        if resp == 'ready':
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            print("VCC is 3.3v fre is %f, duty is %f" %(fre,duty))
            input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            print("VCC is 5v fre is %f, duty is %f" %(fre,duty))
            input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            print("VCC is 2.2v fre is %f, duty is %f" %(fre,duty))
            input("press enter to continue case")
        else:
            return False
        resp = ctx.tester.runCommand("next")

    return True
