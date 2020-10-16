import time
title = "LVD检测"

desc = '''
relay k6,k10 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''

    # 芯片上电VCC=3V
    ctx.netmatrix.arrset(['00000000','01000000','00000000','00000000'])#GP04->vref
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    count = 0
    channel = 3
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_lvd_volt")
    ctx.powersupply.voltageOutput(3, float(resp[:-2])/1000, 0.1, 5, 1)
    vol = float(resp[:-2])
    while resp!= 'end':
        ctx.logger.info(resp)
        if resp == 'ready':
            resp = ctx.tester.runCommand("next")
            time.sleep(0.5)
        if resp =="10mv+":
            vol = vol +0.01
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(channel, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp =="10mv-":
            vol = vol-0.01
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(channel, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp =="1mv-":
            vol = vol -0.001
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(channel, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == "mv" and resp[:6]!= "result" :
            ctx.logger.info ("Right now is " + resp)
            count = count+1
            vol = float(resp[:-2])/1000
            if vol >=2.8:
                ctx.powersupply.voltageOutput(3, 5, 0.1, 5.1, 1)
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(channel, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:6]== "result":
            ctx.logger.info( "final result is %s" %resp[7:])
            input('n')
            if count == 2:
                ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
                channel = 4
            if count == 3:
                ctx.netmatrix.arrset(['00000000','00100000','00000000','00000000'])

            resp = ctx.tester.runCommand("next")
        else :
            return False

    return True
