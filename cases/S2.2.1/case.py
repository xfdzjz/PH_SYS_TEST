
import time
title = "V1P5S线性调整"

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
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("V1P5STest",3)
    counter = 0


    while resp !='end':
        ctx.logger.info(resp)
        if resp == 'ready':
            if counter == 0:
                ctx.logger.info("V1P5S 1.5V")
            else:
                ctx.logger.info("V1P5S 1.2V")
            vol = ctx.sourcemeter.volTest()
            ctx.logger.info("VCC is 3.3v vol is %f" %vol)
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            vol = ctx.sourcemeter.volTest()
            ctx.logger.info("VCC is 5v vol is %f" %vol)
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 6, 1)#voltageOutput(self, channel, V, I, ovp, ocp)
            vol = ctx.sourcemeter.volTest()
            ctx.logger.info("VCC is 2.2v vol is %f" %vol)
            ctx.powersupply.voltageOutput(3, 3.3, 0.1, 6, 1)
            resp = ctx.tester.runCommand("next",2)
            counter = counter +1
        else:
            if counter == 2:  # 此时串口波特率已不正确
                break
            return False

    return True
