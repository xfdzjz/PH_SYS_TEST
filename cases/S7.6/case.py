import time
title = "10V电压校准"

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
    ctx.powersupply.resistor(2,200,13,1)
    ctx.sourcemeter.applyVoltage(3.3)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.oscilloscope.trig(1,"POS",0.4)
    resp = ctx.tester.runCommand("test_dcdc_volt_10p0_volt_trim")
    while resp !='end':
        if resp == "ready1":
            ctx.sourcemeter.applyVoltage(9.5)
            time.sleep(1)
            vol = ctx.powersupply.measure(2, "vol")
            if vol >  8.85 and vol < 10.4:
                ctx.logger.info ("VH output voltage passes %f" %vol)
                ctx.logger.debug ("VH output voltage pass %f" %vol)
            else:
                ctx.logger.info ("VH output voltage failed %f" %vol)
                ctx.logger.debug ("VH output voltage fail %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready2":
            ctx.sourcemeter.applyVoltage(10.5)
            time.sleep(1)
            vol = ctx.powersupply.measure(2, "vol")
            if vol >  9.5 and vol < 11.75:
                ctx.logger.info ("VH output voltage pass %f" %vol)
                ctx.logger.debug ("VH output voltage pass %f" %vol)
            else:
                ctx.logger.info ("VH output voltage fail %f" %vol)
                ctx.logger.debug ("VH output voltage fail %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready3":
            ctx.sourcemeter.applyVoltage(11)
            time.sleep(1)
            vol = ctx.powersupply.measure(2, "vol")
            if vol >  10 and vol < 12.1:
                ctx.logger.info ("VH output voltage pass %f" %vol)
                ctx.logger.debug ("VH output voltage pass %f" %vol)
            else:
                ctx.logger.info ("VH output voltage fail %f" %vol)
                ctx.logger.debug ("VH output voltage fail %f" %vol)
            resp = ctx.tester.runCommand("next")
        elif resp == "ready4":
            resp = ctx.tester.runCommand("next")



    return True
