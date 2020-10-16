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
    ctx.oscilloscope.trig(3,"NEG",1.5,0.001,1)
    ctx.sourcemeter.loadScript()
    time.sleep(0.5)
    resp = 'ready'
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.sourcemeter.runCommand('TSB_Script.run()')
    time.sleep(1)
    resp = ctx.tester.runCommand("test_pd_sensor_out_gain")
    time.sleep(1)
    wave = ctx.oscilloscope.readRamData(2,2,1,15625,'true')

    while resp != 'end':
        if resp == 'ready':

            # print(wave)
            if len(wave) ==1:
                ctx.logger.info('no wave')
                return False
            for i in range(0,len(wave)):
                wave[i] = float(wave[i])
                if wave[i] >2:
                    wave[i] =0

            wave_max = max(wave)
            counter = counter + 1
            ctx.logger.info("wave_max is %f" %wave_max)
            waveMax.append(wave_max)
            count.append(counter)
            ctx.oscilloscope.trig(3,"NEG",1.5,0.01,2)
            time.sleep(1)
            ctx.sourcemeter.runCommand('TSB_Script.run()')
            time.sleep(1)
            resp= ctx.tester.runCommand("next")
            time.sleep(1)
            wave = ctx.oscilloscope.readRamData(2,2,1,15625,'true')
            if counter == 32:
                ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1) # FIXME: check
            if counter == 33:
                ctx.powersupply.voltageOutput(3, 2.2, 0.1, 6, 1) # FIXME: check
            if counter == 34:
                ctx.powersupply.voltageOutput(3, 5, 0.1, 5, 1) # FIXME: check
            if counter == 35:
                ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1) # FIXME: check
        else:
            return False


    return True
