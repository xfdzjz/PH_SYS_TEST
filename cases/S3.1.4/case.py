
import time
title = "bvsMaxCur"

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
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.tester.runCommand("bvsMaxCur")

    amp = ctx.sourcemeter.ampTest()
    ctx.logger.info("I_BVS amp is %f when VCC is 3.3v"%amp)
=======
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("bvsMaxCur")
    if resp == 'ready':
        amp = ctx.sourcemeter.ampTest()
        ctx.logger.info("I_BVS amp is %f when VCC is 3.3v"%amp)
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6


    return True
