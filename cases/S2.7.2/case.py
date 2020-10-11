import time
title = "pdsensor 输出电压"

desc = '''
    relay k1 k15 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
    '''
    waveMax = []
    count = []
    counter = 0

    # 芯片上电VCC=3V
    ctx.netmatrix.arrset(['00000001','00000000','00001000','00000000'])#GP15->osc PDA->src
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(0.250)
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
=======
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    resp = ctx.tester.runCommand("test_pd_sensor_out_gain")

    while resp != 'end':
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp == 'ready':
            ctx.oscilloscope.prepareChannel(2, 1000, 300)
            time.sleep(2)
            ctx.sourcemeter.pulseAmp(0,2e-6,70e-6)
            wave = ctx.oscilloscope.getWave(2, 1000, 300)
            for i in range(0,len(wave)):
                wave[i] = float(wave[i])
            wave_max = max(wave)
            counter = counter + 1
            ctx.logger.info("wave_max is %f" %wave_max)
            waveMax.append(wave_max)
            count.append(counter)
            ctx.logger.info(counter)
            resp = ctx.tester.runCommand("next")
            if counter == 32:
                ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1) # FIXME: check
            if counter == 33:
<<<<<<< HEAD
                ctx.powersupply.voltageOutput(3, 2.2, 0.1, 6, 1) # FIXME: check
            if counter == 34:
                ctx.powersupply.voltageOutput(3, 5, 0.1, 5, 1) # FIXME: check
            if counter == 35:
=======
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
                ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1) # FIXME: check
        else:
            return False


    return True
