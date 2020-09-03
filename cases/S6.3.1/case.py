import time
title = "DCDC 限流功能"

desc = '''
    relay k11 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.sourcemeter  使用
        '''

    vol = 2.5

    # 芯片上电VH=2.5V
    ctx.netmatrix.arrset(['00000000','00000000','00100000','00000000'])
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 4, 1)
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(4, vol, 0.1, 3, 1)


    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_ipk")

    while resp != 'end':
        print(resp)
        if resp == '100mv+':
            vol = vol + 0.1
            ctx.powersupply.voltageOutput(4, vol, 0.1, 3, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:2] == "VH":
            print(resp[:3] + "voltage is %smv" %resp[-4:])
            vol = float(resp[-4:])
            lx_vol = ctx.sourcemeter.volTest()
            Ipk = (vol/1000 -lx_vol)/3
            print("Ipk vol is %f"%Ipk)
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == 'mv':
            vol = float(resp[:-2])
            ctx.powersupply.voltageOutput(4, vol, 0.1, 3, 1)
            resp = ctx.tester.runCommand("next")
        else:
            return False



    return True
