
import time
title = "VDD稳定性测试"

desc = '''
    在时钟trim后做此项测试
    稳压源 Channel3 <=> VCC
    示波器 channel2  <=> GP14
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.netmatrix.arrset(['00000000','00000010','00000000','00000000'])#GP14->OSC
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_volt_ref")
    #resp = ctx.tester.runCommand("next")
    counter =1
    while resp !='end':
        print(resp)
        if resp[0:5] == 'ready':
            ctx.sourcemeter.applyVoltage(2)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            print("VCC is 3.3v avg is %s under M" %(avg))
            #input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            print("VCC is 5v avg is %s under M" %(avg))
            #input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            print("VCC is 2.2v avg is %s under M" %(avg))
            #input("press enter to continue case")
            ctx.powersupply.voltageOutput(3, 3.3, 0.1, 6, 1)
            counter = counter *2
        else:
            return False
        resp = ctx.tester.runCommand("next")

    return True
