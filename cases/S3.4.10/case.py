
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
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.powersupply.voltageOutput(4, 10.5, 0.1, 7, 1)#vh
    ctx.netmatrix.arrset(['00000000','01100000','00000000','00000000'])#Horns,b->osc1,2
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("bzPwmMode")
    if resp == 'ready':
        para1=ctx.oscilloscope.paraTest(1)
        para2=ctx.oscilloscope.paraTest(2)
        if para1[0] == 0.25 and para1[1] == 0.5:
            print("channel1 pass")
        else:
            print("channel1 duty is %f, fre is %f" %(para1[0],para1[1]))
        if para2[0] == 0.25 and para2[1] == 0.5:
            print("channel2 pass")
        else:
            print("channel2 duty is %f, fre is %f" %(para2[0],para2[1]))
        input("press enter to continue")

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True