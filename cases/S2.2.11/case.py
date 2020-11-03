
import time
title = "ISRCA 5uA电流"

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
    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#GP15->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.sourcemeter.applyVoltage(1.2)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("ISRCA5uA",2)
    ctx.logger.info(resp)
    if resp == 'ready':
        amp = ctx.sourcemeter.ampTest() * 1000000
        ctx.logger.info("Isrch amp is %f ua"%amp)


    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        ctx.logger.info(resp)
        return False

    return True
