
import time
title = "ISRCS 60nA电流"

desc = '''
relay k17 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP15->src
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5.0, 1)
<<<<<<< HEAD
    time.sleep(1)
    ctx.sourcemeter.applyVoltage(1.2)

    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("ISRCS60nA",3)
    ctx.logger.info(resp)

    if resp == 'ready':
        amp = ctx.sourcemeter.ampTest()
        print(amp)
        ctx.logger.info("ISRCS amp is %f when VCC is 3.3v"%amp)
        ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
        time.sleep(0.500)
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("ISRCS amp is %f when VCC is 5v"%amp)
        ctx.powersupply.voltageOutput(3, 5, 0.1, 5, 1)
        time.sleep(0.500)
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("ISRCS amp is %f when VCC is 2.2v"%amp)
        resp = ctx.tester.runCommand("next",5)
=======
    time.sleep(0.250)
    ctx.sourcemeter.applyVoltage(1.2)

    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("ISRCS60nA")
    ctx.logger.info(resp)
    if resp == 'ready':
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("ISRCS amp is %f when VCC is 3v"%amp)
        ctx.powersupply.voltageOutput(3, 5, 0.1, 6.0, 1)
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("ISRCS amp is %f when VCC is 5v"%amp)
        ctx.powersupply.voltageOutput(3, 2.2, 0.1, 3.3, 1)
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("ISRCS amp is %f when VCC is 2.2v"%amp)
        resp = ctx.tester.runCommand("next")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6

    if resp!= 'end':
        ctx.logger.info(resp)
        return False

    return True
