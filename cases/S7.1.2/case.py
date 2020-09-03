import time
title = "4.5V带载"

desc = '''
    relay k4,k15 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
        '''


    # 芯片上电VCC=3V

    ctx.netmatrix.arrset(['00000000','00000000','00010000','10000000'])#GP00 ->osc1 gp14->osc2
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 4, 1)
    time.sleep(250)
    ctx.powersupply.channelOn(1)
    ctx.powersupply.channelOn(2)
    ctx.powersupply.voltageOutput(1, 4.5, 0.1, 4, 1)
    ctx.tester.runCommand("test_mode_sel")
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
