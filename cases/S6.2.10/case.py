import time
title = "DCDC VOOK功能"

desc = '''
    relay k11 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
        '''

    vol = 3

    # 芯片上电VCC=3V
    ctx.sourcemeter.applyVoltage(3)
    ctx.netmatrix.arrset(['00000000','00000000','00100000','00000000'])
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_vok")



    while resp != 'end':
        print(resp)
        if resp == '100mv+':
            ctx.sourcemeter.applyVoltage(vol + 0.1)
            resp = ctx.tester.runCommand("next")
        elif resp == '100mv-':
            ctx.sourcemeter.applyVoltage(vol - 0.1)
            resp = ctx.tester.runCommand("next")
        elif resp[:3] == "vok":
            print(resp[:4] + "voltage is %sv" %resp[-5:-2])
            vol = float(resp[-5:-2])
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == 'mv':
            vol = float(resp[:-2])
            ctx.sourcemeter.applyVoltage(vol)
            resp = ctx.tester.runCommand("next")
        else:
            return False



    return True
