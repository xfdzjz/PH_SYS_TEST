
import time
title = "	ADC采样输入通道遍历2"

desc = '''
    relay k25 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])#GP19->SRC case5 AIN00
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    input('m')
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_adc_chn0_samp")

    ctx.logger.info(resp)
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
    #resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False


    ctx.netmatrix.arrset(['00100000','00000000','00000000','00000000'])#GP04->SRC case5 AIN01
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_adc_chn2_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

    #resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#GP05->SRC case5
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    resp = ctx.tester.runCommand("test_adc_chn3_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

    #resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    ctx.netmatrix.arrset(['10000000','00000000','00000000','00000000'])#GP01->SRC case5
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    resp = ctx.tester.runCommand("test_adc_chn4_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

    #resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP08->SRC case5
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    resp = ctx.tester.runCommand("test_adc_chn7_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

    #resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    ctx.netmatrix.arrset(['00000100','00000000','00000000','00000000'])#GP14->SRC case5
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    resp = ctx.tester.runCommand("test_adc_chn10_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
    #resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False


    ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])#GP02->SRC case5
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    resp = ctx.tester.runCommand("test_adc_chn11_samp")
    if resp == 'ready':
        ctx.sourcemeter.applyVoltage(0.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

        ctx.sourcemeter.applyVoltage(1.5)
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)

   # resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
