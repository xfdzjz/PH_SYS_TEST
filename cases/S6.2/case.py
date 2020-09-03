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

    ctx.netmatrix.arrset(['00000000','00000000','00010000','00000000'])
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 7, 1)#vCC
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(2, 3, 0.1, 7, 1)#vh
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_vok")



    while resp != 'end':
        print(resp)
        if resp == '100mv+':
            ctx.powersupply.voltageOutput(2, vol + 0.1, 0.1, 7, 1)
            resp = ctx.tester.runCommand("next")
        elif resp == '100mv-':
            ctx.powersupply.voltageOutput(2, vol - 0.1, 0.1, 7, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:3] == "vok":
            print(resp[:4] + "voltage is %sv" %resp[-5:-2])
            vol = float(resp[-5:-2])
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == 'mv':
            vol = float(resp[:-2])
            ctx.powersupply.voltageOutput(2, vol, 0.1, 7, 1)
            resp = ctx.tester.runCommand("next")
        else:
            return False



    return True
