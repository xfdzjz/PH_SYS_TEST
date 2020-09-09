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
    ctx.netmatrix.arrset(['00000000','00000000','00100000','00000000'])#lx->osc1 gp14->osc2
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 4, 1)
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(4, vol, 0.1, 10, 1)
    ctx.oscilloscope.trigMul(2,'POS',0.7, scale = 0.01)


    #ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_dcdc_ipk")
    time.sleep(3)

    while resp != 'end':
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp == '100mv+':
            vol = vol + 100
            ctx.powersupply.voltageOutput(4, vol/1000, 0.1, 10, 1)
            resp = ctx.tester.runCommand("next")
        elif resp[:2] == "VH":
            ctx.logger.info(resp[:3] + "voltage is %smv" %resp[-4:])
            vol = float(resp[-4:])
            if ctx.oscilloscope.statusCheck() ==True:
                vol1 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
                vol2 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
                for i in range (0, len(vol2)):
                    if float(vol2[i]) >=1.2:
                        lx_vol = float(vol1[i])
                    else:
                        ctx.logger.info("GP14 test fail")
                        return False
            else:
                ctx.logger.info("V1 test fail")
                return False

            Ipk = (vol/1000 -lx_vol)/3
            ctx.logger.info("Ipk vol is %f"%Ipk)
            resp = ctx.tester.runCommand("next")
        elif resp[-2:] == 'mv':
            vol = float(resp[:-2])
            ctx.powersupply.voltageOutput(4, vol, 0.1, 10, 1)
            resp = ctx.tester.runCommand("next")

        else:
            return False



    return True
