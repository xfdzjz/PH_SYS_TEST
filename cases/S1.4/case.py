
import time
title = "HRC自动trim流程"

desc = '''
relay has no connection
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=3
    ctx.netmatrix.arrset(['00000000','00000000','00000000','00000000'])
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(0.25)
<<<<<<< HEAD
    resp = ctx.tester.runCommand("TestHrcTrim",2)
=======

    resp = ctx.tester.runCommand("TestHrcTrim")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    ctx.logger.info(resp)
    while resp != 'end':
        if resp == 'fail':
            return False
<<<<<<< HEAD
        resp = ctx.tester.runCommand("next",2)
        ctx.logger.info(resp)
=======
        resp = ctx.tester.runCommand("next")
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    return True
