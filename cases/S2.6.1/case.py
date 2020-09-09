
import time
title = "indLed导通压降"

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
    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP15->src
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(0.250)
    ctx.sourcemeter.applyVoltage(3.3-0.5)
    #ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("indLedOnVoltDrop")
    ctx.logger.info(resp)
    ctx.logger.debug(resp)
    #if resp == 'ready':
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("indled amp is %f when VCC is 3v"%amp)
    ctx.powersupply.voltageOutput(3, 5, 0.1, 3.3, 1)
    ctx.sourcemeter.applyVoltage(5-0.5) # FIXME: check and fix
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("indled amp is %f when VCC is 5v"%amp)
    ctx.powersupply.voltageOutput(3, 2.2, 0.1, 3.3, 1)
    ctx.sourcemeter.applyVoltage(2.2-0.5) # FIXME: check and fix
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("indled amp is %f when VCC is 2.2v"%amp)

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        ctx.logger.info(resp)
        return False

    return True
