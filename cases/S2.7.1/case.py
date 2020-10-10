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

    ctx.oscilloscope.prepareChannel(2, 1000, 300)
    ctx.oscilloscope.runsta()
    resp ='ready'
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.tester.runCommand("test_pd_sensor_out_volt")

    while resp != 'end':
        if resp == 'ready':
            ctx.sourcemeter.pulseAmp(0,1e-9,70e-6)
            time.sleep(1)
            wave = ctx.oscilloscope.getWave(2, 1000, 300)
            wave1 = ctx.oscilloscope.readRamData(2,2,1,15625,'true')
            print(wave1)
            for i in range(0,len(wave)):
                wave[i] = float(wave[i])
                if wave[i] >3:
                    wave[i] =0
            wave_max = max(wave)
            counter = counter + 1
            ctx.logger.info("wave_max is %f" %wave_max)
            waveMax.append(wave_max)
            count.append(counter)
            resp = ctx.tester.runCommand("next")
        else:
            return False
        input('n')
    #ctx.logger.info(count)

    ctx.logger.info(waveMax)

    ctx.sourcemeter.applyCurrent(1e-9)
    input('n')
    return True
