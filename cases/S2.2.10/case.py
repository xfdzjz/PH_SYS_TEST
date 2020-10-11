
import time
title = "ISRCH 1.2uA电流"

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
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(0.250)
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
=======
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    resp = ctx.tester.runCommand("ISRCH1p2uA")
    ctx.logger.info(resp)
    ctx.logger.debug(resp)
    if resp == 'ready':
        vol = ctx.sourcemeter.volTest()
        ctx.logger.info("Visrch vol is %f"%vol)

    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        ctx.logger.info(resp)
        return False

    return True
