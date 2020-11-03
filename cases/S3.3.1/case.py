
import time
title = "Thermdrv导通压降"

desc = '''
    relay k1 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1

    ctx.netmatrix.arrset(['10000000','00000000','00000000','00000000'])#GP12->SRC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.4, 1)
    ctx.sourcemeter.applyVoltage(0.2)

    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("thermdrvOnVoltDrop",3)
    if resp == 'ready':
        amp = ctx.sourcemeter.ampTest() * 1000
        ctx.logger.info("thermdrv amp is %f mA when VCC is 3v"%amp)
        ctx.powersupply.voltageOutput(3, 2.2, 0.1, 3.3, 1)
        amp = ctx.sourcemeter.ampTest() * 1000
        ctx.logger.info("thermdrv amp is %f mA when VCC is 2.2v"%amp)
        ctx.powersupply.voltageOutput(3, 5, 0.1, 3.3, 1)
        amp = ctx.sourcemeter.ampTest() * 1000
        ctx.logger.info("thermdrv amp is %f mA when VCC is 5v"%amp)
        input('n')


    resp = ctx.tester.runCommand("next",2)
    # ctx.logger.debug(resp)
    return True
