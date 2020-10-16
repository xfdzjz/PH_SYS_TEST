
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
    ctx.netmatrix.arrset(['10000000','00000000','00000000','00000000'])#GP15->src

    ctx.powersupply.voltageOutput(3, 3.3, 0.5, 5.1, 1)
    ctx.sourcemeter.applyVoltage(3.3-0.5)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("indLedOnVoltDrop",3)
    ctx.logger.info(resp)
    if resp == 'ready':
        amp = ctx.sourcemeter.ampTest()
        input('n')
        ctx.logger.info("indled amp is %f when VCC is 3.3v"%amp)
        ctx.powersupply.voltageOutput(3, 2.2, 0.5, 5.1, 1)
        ctx.sourcemeter.applyVoltage(2.2-0.5) # FIXME: check and fix
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("indled amp is %f when VCC is 2.2v"%amp)
        ctx.powersupply.voltageOutput(3, 5, 0.5, 5.1, 1)
        ctx.sourcemeter.applyVoltage(5-0.5) # FIXME: check and fix
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("indled amp is %f when VCC is 5v"%amp)


    resp = ctx.tester.runCommand("next",3)
    if resp!= 'end':
        ctx.logger.info(resp)
        return False

    return True
