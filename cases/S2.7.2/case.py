import time
title = "pdsensor 输出电压"

desc = '''
    源表 <=> PDAS
    稳压源 <=> VCC
    示波器 <=> GP15(VO1)
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
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    ctx.netmatrix.arrset(['00000000','00000000','00001000','00000000'])#GP15->OSC
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_pd_sensor_out_gain")

    while resp != 'end':

        if resp == 'ready':
            ctx.sourcemeter.pulseAmp(0,2e-6,70e-6)
            ctx.oscilloscope.prepareChannel(3, 1000, 300)
            wave = ctx.oscilloscope.getWave(3, 1000, 300)
            wave_max = max(wave)
            counter = counter + 1
            print("wave_max is %f" %wave_max)
            waveMax.append(wave_max)
            count.append(counter)
            resp = ctx.tester.runCommand("next")
            print(resp)
            if counter == 2:
                resp = ctx.tester.runCommand("next")
            #input("press Enter to continue")
        else:
            return False


    return True
