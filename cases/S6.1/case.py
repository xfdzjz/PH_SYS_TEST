import time
title = "DCDC占空比"

desc = '''
    relay k11 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
    '''

    # 芯片上电VCC=3V

    ctx.netmatrix.arrset(['00000000','00000000','00010000','00000000'])# NO 2 relay

    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(2, 3.0, 0.1, 5, 1)
    ctx.oscilloscope.prepareChannel(2, 1000, 300)
    ctx.oscilloscope.runsta()
    resp = ' '
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_dcdc_duty")


    while resp != 'end':
        ctx.oscilloscope.runsta()
        if resp == 'ready':
            time.sleep(2)

            #wave = ctx.oscilloscope.getWave(2, 1000, 300)
            para = ctx.oscilloscope.paraTest(2)
            duty = 100*float(para[0])
            freq = float(para[1])

            input('n')
            ctx.logger.info("duty is %f percent, frequency is %f"%(duty,freq))
            ctx.logger.debug("duty is %f percent, frequency is %f"%(duty,freq))
            #ctx.logger.info(wave)
            resp = ctx.tester.runCommand("next")
        else:
            return False



    return True
