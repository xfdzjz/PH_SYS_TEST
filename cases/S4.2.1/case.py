
import time
title = "ADC通道遍历1"

desc = '''
    relay k31 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1

    ctx.netmatrix.arrset(['00000001','00000000','00000000','00000000'])#GP18->SRC case4
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_adc_chn1_samp")
    if resp != 'ready':
        return False

    ctx.sourcemeter.applyVoltage(0.5)
    resp = ctx.tester.runCommand("next")
    ctx.logger.debug(resp)

    ctx.sourcemeter.applyVoltage(1.5)
    resp = ctx.tester.runCommand("next")
    ctx.logger.debug(resp)

    ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])#GP06->SRC case4
    resp = ctx.tester.runCommand("test_adc_chn5_samp")
    if resp != 'ready':
        return False
    ctx.sourcemeter.applyVoltage(0.5)
    resp = ctx.tester.runCommand("next")
    ctx.logger.debug(resp)

    ctx.sourcemeter.applyVoltage(1.5)
    resp = ctx.tester.runCommand("next")
    ctx.logger.debug(resp)
    if resp!= 'end':
        return False

    ctx.netmatrix.arrset(['00100000','00000000','00000000','00000000'])#GP07->SRC case4
    resp = ctx.tester.runCommand("test_adc_chn6_samp")
    if resp != 'ready':
        return False
    ctx.sourcemeter.applyVoltage(0.5)
    resp = ctx.tester.runCommand("next")

    ctx.logger.debug(resp)
    ctx.sourcemeter.applyVoltage(1.5)
    resp = ctx.tester.runCommand("next")

    ctx.logger.debug(resp)
    if resp!= 'end':
        return False

    ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#GP10->SRC case4
    resp = ctx.tester.runCommand("test_adc_chn8_samp")
    if resp != 'ready':
        return False
    ctx.sourcemeter.applyVoltage(0.5)
    resp = ctx.tester.runCommand("next")

    ctx.logger.debug(resp)
    ctx.sourcemeter.applyVoltage(1.5)
    resp = ctx.tester.runCommand("next")

    ctx.logger.debug(resp)
    if resp!= 'end':
        return False

    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP011->SRC case4
    resp = ctx.tester.runCommand("test_adc_chn9_samp")
    if resp != 'ready':
        return False
    ctx.sourcemeter.applyVoltage(0.5)
    resp = ctx.tester.runCommand("next")

    ctx.logger.debug(resp)
    ctx.sourcemeter.applyVoltage(1.5)
    resp = ctx.tester.runCommand("next")

    ctx.logger.debug(resp)
    if resp!= 'end':
        ctx.logger.info("case 4.2.1 fail")
        return False
    ctx.logger.info("case 4.2.1 pass")
    return True
