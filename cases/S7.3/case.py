import time
title = "5.5V纹波、带载"

desc = '''
    relay k4,k15 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
        '''

    vol = 3

    # 芯片上电VCC=3V

    ctx.netmatrix.arrset(['00000000','00000000','00010000','10000000'])#GP00 ->osc1 gp14->osc2
    ctx.powersupply.voltageOutput(1, 3.3, 0.1, 4, 1)
    ctx.powersupply.voltageOutput(2, 0, 0.1, 10, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.oscilloscope.trig(1,"POS",0.4)
    resp = ctx.tester.runCommand("test_dcdc_volt_5p5_volt_trim")
    while resp !='end':
        if resp == "ready1":
            ctx.sourcemeter.applyVoltage(5.21)
            time.sleep(1)
            vol =(ctx.powersupply.measure(2, "vol"))
            if vol >  4.7 and vol < 5.75:
                ctx.logger.info ("VH output voltage passes %f" %vol)
                ctx.logger.debug("VH output voltage pass %f" %vol)
            else:
                ctx.logger.info ("VH output voltage fail %f" %vol)
                ctx.logger.debug("VH output voltage failed %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready2":
            ctx.sourcemeter.applyVoltage(5.78)
            time.sleep(1)
            vol = (ctx.powersupply.measure(2, "vol"))

            if vol >  5.1 and vol < 6.2:
                ctx.logger.info ("VH output voltage pass %f" %vol)
                ctx.logger.debug("VH output voltage pass %f" %vol)
            else:
                ctx.logger.info ("VH output voltage failed %f" %vol)
                ctx.logger.debug("VH output voltage failed %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready3":
            ctx.sourcemeter.applyVoltage(6.03)
            time.sleep(1)
            vol = (ctx.powersupply.measure(2, "vol"))

            if vol >  5.4 and vol < 6.6525:
                ctx.logger.info ("VH output voltage pass %f" %vol)
                ctx.logger.debug("VH output voltage pass %f" %vol)
            else:
                ctx.logger.info ("VH output voltage failed %f" %vol)
                ctx.logger.debug("VH output voltage failed %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready4":
            resp = ctx.tester.runCommand("next")



    return True
