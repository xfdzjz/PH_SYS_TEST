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
    time.sleep(0.250)
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_lvd_volt")
    ctx.powersupply.voltageOutput(3, float(resp[:-2])/1000, 0.1, 5, 1)
    vol = float(resp[:-2])
    while resp!= 'end':
=======
    #ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_lvd_volt")
    ctx.logger.info(resp)
    ctx.powersupply.voltageOutput(3, float(resp[:-2]), 0.1, 5, 1)
    vol = float(resp[:-2])
    while resp!= 'end':

>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
        ctx.logger.info(resp)
        if resp == 'ready':
            resp = ctx.tester.runCommand("next")
        if resp =="10mv+":
            vol = vol +0.01
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp =="10mv-":
            vol = vol-0.01
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp =="1mv-":
            vol = vol -0.001
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == "mv" and resp[:6]!= "result" :
            ctx.logger.info ("Right now is " + resp)
            vol = float(resp[:-2])/1000
<<<<<<< HEAD
            if vol >=2.8:
                ctx.powersupply.voltageOutput(3, 5, 0.1, 5.1, 1)
=======
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
            ctx.logger.info(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:6]== "result":
            ctx.logger.info( "final result is %s" %resp[7:])
            resp = ctx.tester.runCommand("next")
        else :
            return False

    return True
