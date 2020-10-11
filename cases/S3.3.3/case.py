
import time
title = "LEDDRV电流值"

desc = '''
relay k13,k17 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#BLED->SRC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(2, 5.7, 0.1, 7, 1)#vh
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
=======
    #ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    resp = ctx.tester.runCommand("ledDrive")
    if resp != 'ready':
        return False

    ctx.sourcemeter.applyVoltage(2)
    amp = ctx.sourcemeter.ampTest()
<<<<<<< HEAD
    ctx.logger.info("Ibled amp is %f when VCC is 3.3v"%amp)
    ctx.logger.debug("Ibled amp is %f when VCC is 3.3v"%amp)
=======
    ctx.logger.info("Ibled amp is %f when VCC is 3v"%amp)
    ctx.logger.debug("Ibled amp is %f when VCC is 3v"%amp)
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    resp = ctx.tester.runCommand("next")
    if resp != 'ready':
        return False

    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#BLED->SRC
    amp = ctx.sourcemeter.ampTest()
<<<<<<< HEAD
    ctx.logger.info("Irbled amp is %f when VCC is 3.3v"%amp)
    ctx.logger.debug("Irbled amp is %f when VCC is 3.3v"%amp)
    resp = ctx.tester.runCommand("next",2)

=======
    ctx.logger.info("Ibled amp is %f when VCC is 3v"%amp)
    ctx.logger.debug("Ibled amp is %f when VCC is 3v"%amp)
    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6

    return True
