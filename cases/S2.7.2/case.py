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
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_pd_sensor_out_gain")

    while resp != 'end':
        print(resp)
        if resp == 'ready':
            ctx.oscilloscope.prepareChannel(3, 1000, 300)
            ctx.sourcemeter.pulseAmp(0,2e-6,70e-6)
            wave = ctx.oscilloscope.getWave(3, 1000, 300)
            wave_max = max(wave)
            counter = counter + 1
            print("wave_max is %f" %wave_max)
            waveMax.append(wave_max)
            count.append(counter)
            resp = ctx.tester.runCommand("next")
            if counter == 2:
                resp = ctx.tester.runCommand("next") # FIXME: check
        else:
            return False


    return True
