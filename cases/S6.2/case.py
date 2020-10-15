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
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5.5, 1)#vCC
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(2, 3, 0.1, 7, 1)#vh
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_dcdc_vok")

    ctx.oscilloscope.staReco()

    while resp != 'end':
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp == '100mv+':
            vol = vol + 100
            ctx.powersupply.voltageOutput(2, vol/1000 , 0.1, 7, 1)
            ctx.logger.info(vol)
            resp = ctx.tester.runCommand("next")
        elif resp == '100mv-':
            vol = vol - 100
            ctx.powersupply.voltageOutput(2, vol/1000 , 0.1, 7, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:3] == "vok":
            ctx.logger.info(resp[:4] + "vol is %sv" %resp[-5:-2])
            vol = float(resp[-5:-2])
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == 'mv':
            vol = float(resp[:-2])
            ctx.powersupply.voltageOutput(2, vol/1000, 0.1, 7, 1)
            resp = ctx.tester.runCommand("next")
        else:
            return False



    return True
