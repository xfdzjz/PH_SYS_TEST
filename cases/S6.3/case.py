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

    vol = 0

    # 芯片上电VH=2.5V
    ctx.netmatrix.arrset(['00000000','00000000','00010000','00000000'])#lx->osc1 gp14->osc2
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 4, 1)
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(2, vol, 0.2, 10, 1)
    ctx.powersupply.ocp(2, 1.6)
    ctx.powersupply.ovp(2, 4.55)
    ctx.powersupply.iset(2, 1.5)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_dcdc_ipk")





    while resp != 'end':
        vol2 =[]
        vol1 =[]
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp == 'ready':
            vol = 0.5
            ctx.powersupply.voltageOutput(2, vol, 0.2, 10, 1)
            time.sleep(2)
            ctx.oscilloscope.trigMul(2,'POS',2.3, scale = 1e-6)
            time.sleep(2)
            #input('n')
            while len(vol2) ==0:
                if vol < 4.5:
                    ctx.powersupply.voltageOutput(2, vol, 0.2, 10, 1)
                    if ctx.oscilloscope.statusCheck() == True:
                        vol2 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
                        vol1 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
                        print(vol1)
                        print(vol2)
                    else:
                        vol = vol+0.1
                else:
                    return False

            for i in range (0, len(vol2)):
                vol2[i] = float(vol2[i])
                if vol2[i] >= 2.1:
                    lx_vol = float(vol1[i])
                    break
                if i ==len(vol2)-2 and vol2[i] < 2.1:
                    return False
            print("i=%d, len(vol2)=%d" % (i, len(vol2)))
            for j in range(i,0,-1):
                current_vol = float(vol1[j+1])
                last_vol = float(vol1[j])
                print(current_vol, last_vol)
                if current_vol < last_vol and last_vol < 1.5:
                    ctx.logger.info("LX neg val is %f when VH is %f" %(last_vol,vol))
                    break
            if j == 0:
                ctx.logger.info("there is no neg val")
                return False
            ctx.oscilloscope.runsta()
            Ipk = (vol  - lx_vol)/3
            ctx.logger.info("Ipk vol is %f"%Ipk)
            resp = ctx.tester.runCommand("next")


    return True
