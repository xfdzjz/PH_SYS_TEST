
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
    ctx.netmatrix.arrset(['00000000','00000000','00010000','00000000'])#GP14->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("MRCTestOnVCCVerify",3)
    ctx.oscilloscope.timeset(0.0000005)#示波器x轴一格多宽

    while resp !='end':
        ctx.logger.info(resp)
        if resp == 'ready':
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            ctx.logger.info("VCC is 3.3v fre is %f, duty is %f" %(fre,duty))
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 6, 1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            ctx.logger.info("VCC is 2.2v fre is %f, duty is %f" %(fre,duty))
            ctx.powersupply.voltageOutput(3, 5, 0.1, 5, 1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            ctx.logger.info("VCC is 5v fre is %f, duty is %f" %(fre,duty))
        else:
            return False
        resp = ctx.tester.runCommand("next",1)

    return True
