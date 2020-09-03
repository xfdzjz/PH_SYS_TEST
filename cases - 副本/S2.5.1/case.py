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
    ctx.netmatrix.arrset(['00000000','01100000','00000000','00000000'])#GP05,04->vref
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_lvd_volt")
    print("resp is %s" %resp)
    ctx.powersupply.voltageOutput(3, float(resp[:-2]), 0.1, 5, 1)
    vol = float(resp[:-2])
    while resp!= 'end':
        print("resp is %s" %resp)
        if resp =="10mv+":
            vol = vol +0.01
            print(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp =="10mv-":
            vol = vol-0.01
            print(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp =="1mv-":
            vol = vol -0.001
            print(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == "mv" and resp[:6]!= "result" :
            print ("Right now is " + resp)
            vol = float(resp[:-2])/1000
            print(vol)
            ctx.powersupply.voltageOutput(3, vol, 0.1, 5, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:6]== "result":
            print( "final result is %s" %resp[7:])
            resp = ctx.tester.runCommand("next")
        else :
            return False

    return True
