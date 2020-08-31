import time
title = "DCDC VOOK功能"

desc = '''
    源表 <=> PDAS
    稳压源channel2 <=> VCC
    示波器 <=> GP15(VO1)
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
        '''


    # 芯片上电VCC=3V
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 4, 1)
    ctx.netmatrix.arrset(['10000000','01000000','00100000','00010000'])
    ctx.powersupply.channelOn(1)
    ctx.powersupply.channelOn(2)
    ctx.powersupply.voltageOutput(1, 4.5, 0.1, 4, 1)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_volt_4p5ipk")
    ctx.sourcemeter.applyCurrent(0.01)
    while resp !='end':
        if resp == "ready":

            ctx.powersupply.channelOn(1)
            curr = ctx.powersupply.measure(1,"CURRent")
            print("current is %s ampere" %curr)
            resp = ctx.tester.runCommand("next")
        else:
            return False



    return True
