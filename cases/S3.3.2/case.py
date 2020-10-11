
import time
title = "BZ导通压降"

desc = '''
relay k5, k9 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['01000000','00000010','00000000','00000000'])#HORNS->SRC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(2, 10.5, 0.1, 3.3, 1)#vh
    ctx.powersupply.voltageOutput(4, 0, 0.1, 3.3, 1)#FI
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
=======
    #ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    resp = ctx.tester.runCommand("bzOnVoltDrop")
    ctx.logger.info(resp)
    if resp != 'ready':
        return False

    ctx.sourcemeter.applyVoltage(0.5)
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_BZNS amp is %f when sourmeter is 0.5v"%amp)
    ctx.logger.debug("I_BZNS amp is %f when sourmeter is 0.5v"%amp)
    resp = ctx.tester.runCommand("next")
    if resp != 'ready':
        return False

    ctx.sourcemeter.channel('off')
    time.sleep(3)
    ctx.netmatrix.arrset(['00100000','00000000','00000000','00000000'])#HORNB->SRC
<<<<<<< HEAD
    ctx.sourcemeter.applyVol(10)
=======
    ctx.sourcemeter.applyVoltage(10)
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    ctx.sourcemeter.channel('on')
    time.sleep(3)
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_BZPB amp is %f when sourmeter is 10v"%amp)
    ctx.logger.debug("I_BZPB amp is %f when sourmeter is 10v"%amp)
    resp = ctx.tester.runCommand("next")
    if resp != 'ready':
        return False

    ctx.netmatrix.arrset(['00000000','00000010','00000000','00000000'])
    ctx.powersupply.voltageOutput(4, 10.5, 0.1, 12, 1)
    ctx.netmatrix.arrset(['01000000','00000010','00000000','00000000'])#HORNS->SRC
<<<<<<< HEAD
    ctx.sourcemeter.applyVol(10)
=======
    ctx.sourcemeter.applyVoltage(10)
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_BZPS amp is %f when sourmeter is 10v"%amp)
    ctx.logger.debug("I_BZPS amp is %f when sourmeter is 10v"%amp)
    resp = ctx.tester.runCommand("next")
    if resp != 'ready':
        return False

    ctx.sourcemeter.channel('off')
    time.sleep(3)
    ctx.netmatrix.arrset(['00100000','00000010','00000000','00000000'])#HORNB->SRC
    ctx.sourcemeter.applyVoltage(0.5)
    ctx.sourcemeter.channel('on')
    time.sleep(3)
    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_BZNB amp is %f when sourmeter is 0.5v"%amp)
    ctx.logger.debug("I_BZNB amp is %f when sourmeter is 0.5v"%amp)
    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
