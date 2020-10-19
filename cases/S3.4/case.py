
import time
title = "BZ pwm功能"

desc = '''
relay k6,k10 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1

    ctx.netmatrix.arrset(['00000000','00000010','01000000','00100000'])#Horns,b->osc1,2
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.powersupply.voltageOutput(2, 10.5, 0.1, 11, 1)#vh
    ctx.oscilloscope.trigMul(2,"POS",0.5,0.01,2)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("bzPwmMode",2)
    ctx.oscilloscope.timeset(0.0002)
    if resp == 'ready':
        time.sleep(2)
        para1=ctx.oscilloscope.paraTest(1)
        time.sleep(1)
        para2=ctx.oscilloscope.paraTest(2)
        time.sleep(1)
        if para1[0] == 0.25 and para1[1] == 0.5:
            ctx.logger.info("channel1 pass")
        else:
            ctx.logger.info("channel1 duty is %f, fre is %f" %(para1[0],para1[1]))
        if para2[0] == 0.25 and para2[1] == 0.5:
            ctx.logger.info("channel2 pass")
        else:
            ctx.logger.info("channel2 duty is %f, fre is %f" %(para2[0],para2[1]))


    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
