import time
title = "LVD检测"

desc = '''
    relay k5,k14 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''

    # 芯片上电VCC=3V
    ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])#GP04->src

    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_ref_sel",2)
    count = 0

    while resp!='end':
        ctx.logger.info(resp)
        if resp =='ready':
            ctx.logger.debug(resp)
        if count %2 == 0:
            ctx.sourcemeter.applyVoltage(0.5)
            count = count + 1
            resp = ctx.tester.runCommand("next")
        elif count %2 ==1:
            ctx.sourcemeter.applyVoltage(1.5)
            count = count + 1
            resp = ctx.tester.runCommand("next")
            ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])##GP04->src,GP14->vref
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 5, 1)
        else :
            return False
    print('pass')
    return True
