
import time
title = "Voltref模块"

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
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_volt_ref")
    #resp = ctx.tester.runCommand("next")

    while resp !='end':
        print(resp)
        counter =2
        if resp[0:5] == 'ready':
            ctx.sourcemeter.applyVoltage(2)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            print("VCC is 3.3v avg is %s under %dM" %(avg,counter))
            #input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            print("VCC is 5v avg is %s under %dM" %(avg,counter))
            #input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            print("VCC is 2.2v avg is %s under %dM" %(avg,counter))
            #input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 3.3, 0.1, 6, 1)
            counter = counter *2
        else:
            return False
        resp = ctx.tester.runCommand("next")

    return True
