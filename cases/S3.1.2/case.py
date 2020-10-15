
import time
title = "pwrdown功耗"

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

    ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])#VCC->SRC
    ctx.sourcemeter.applyVoltage(3.3)
    time.sleep(0.250)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.tester.runCommand("DeepSleep")

    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_dsleep amp is %f when VCC is 3v"%amp)
    ctx.sourcemeter.applyVoltage(5)
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_dsleep amp is %f when VCC is 5v"%amp)
    ctx.sourcemeter.applyVoltage(2.2)
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_dsleep amp is %f when VCC is 2.2v"%amp)
    ctx.sourcemeter.applyVoltage(3.3)
    return True
