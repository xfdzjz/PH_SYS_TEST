
import time
title = "V1P5D线性调整"

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
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("V1P5DTest")
    counter = 0


    while resp !='end':
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp == 'ready':
            if counter== 0:
                ctx.logger.info("V1P5D 1.5V")
            else:
                ctx.logger.info("V1P5D 1.2V")
            vol = ctx.sourcemeter.volTest()
            ctx.logger.info("VCC is 3.3v vol is %f" %vol)
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            vol = ctx.sourcemeter.volTest()
            ctx.logger.info("VCC is 5v vol is %f" %vol)
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            vol = ctx.sourcemeter.volTest()
            ctx.logger.info("VCC is 2.2v vol is %f" %vol)
            ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
            counter = counter +1
        else:
            return False

    return True
