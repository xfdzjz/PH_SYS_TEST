
import time
title = "Voltref模块"

desc = '''
 relay k15 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#GP14->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_volt_ref",3)
    a =[2500,2000,1500,1200]
    i = 0

    while resp !='end':
        ctx.logger.info(resp)
        if resp[0:5] == 'ready':
            time.sleep(1)
            avg = ctx.sourcemeter.volTest()
            ctx.logger.info("%d VCC is 3.3v avg is %s" %(a[i],avg))
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            avg = ctx.sourcemeter.volTest()
            ctx.logger.info("%d VCC is 5v avg is %s" %(a[i],avg))
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            avg = ctx.sourcemeter.volTest()
            ctx.logger.info("%d VCC is 2.2v avg is %s" %(a[i],avg))
            ctx.powersupply.voltageOutput(3, 3.3, 0.1, 6, 1)
            i=i+1
        else:
            return False
        resp = ctx.tester.runCommand("next")

    return True
