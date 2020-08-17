import time
title = "LVD检测"

desc = '''
    在时钟trim后做此项测试
    稳压源 Channel1 <=> VCC
    稳压源 Channel2 <=> GP18
    源表 <=> GP00
'''


def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''

    # 芯片上电VCC=3V
    ctx.sourcemeter.applyVoltage(3)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_lvd_volt")
    ctx.powersupply.voltageOutput(1, int(resp[:-2]), 0.1, 5, 1)
    vol = float(resp[:-2])
    while resp != 'end':
        if resp == "10mv+":
            resp = vol + 0.01
            ctx.powersupply.voltageOutput(1, resp, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp == "10mv-":
            resp = vol-0.01
            ctx.powersupply.voltageOutput(1, resp, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp == "1mv-":
            resp = vol - 0.001
            ctx.powersupply.voltageOutput(1, resp, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == "mv":
            print("Right now is " + resp)
            vol = float(resp[:-2])/1000
            print(vol)
            ctx.powersupply.voltageOutput(1, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:6] != "result":
            print("final result is %s" % resp[7:])
            resp = ctx.tester.runCommand("next")
        else:
            return False

    return True
