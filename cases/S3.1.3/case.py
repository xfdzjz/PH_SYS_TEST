
import time
title = "PowerDown功耗"

desc = '''
    relay k25 connect
'''
POWERON_DELAY = 2
def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1

    ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])#VCC->SRC
    ctx.sourcemeter.applyVoltage(3.3)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)

    ctx.tester.runCommand("PowerDown",POWERON_DELAY + 1)
    # amp = ctx.sourcemeter.ampTest() * 1000
    # ctx.logger.info("I_pwrdown amp is %f mA when VCC is 5v"%amp)

    # ctx.sourcemeter.applyVoltage(3.3)
    time.sleep(POWERON_DELAY)
    amp = ctx.sourcemeter.ampTest() * 1000
    ctx.logger.info("I_pwrdown amp is %f mA when VCC is 3.3v"%amp)

    # ctx.sourcemeter.applyVoltage(2.2)
    # time.sleep(POWERON_DELAY)
    # amp = ctx.sourcemeter.ampTest() * 1000
    # ctx.logger.info("I_pwrdown amp is %f mA when VCC is 2.2v"%amp)

    return True
