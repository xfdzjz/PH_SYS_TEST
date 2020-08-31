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
    ctx.powersupply.voltageOutput(1, 3.3, 0.1, 4, 1)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_xtl")
    while resp !='end':
        if resp == "ready":
            resp = ctx.tester.runCommand("next")
        else:
            return False

    return True
