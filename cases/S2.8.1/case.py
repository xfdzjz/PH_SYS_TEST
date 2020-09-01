import time
title = "ADC采样速率遍历4MHz~500KHz"

desc = '''
    relay k5,k14 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''
    count = 0
    step = 0
    ad_vol = []
    counter = []
    # 芯片上电VCC=3V
    #ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])#GP04->src GP14->vref
    ctx.sourcemeter.applyVoltage(3.3)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_freq")
    resp = ctx.tester.runCommand("next") # FIXME: check

    while resp !="end":
        print(resp)
        if resp[-2:] == 'mv':
            vol = float(resp[:-2])
            step = vol / 4096
        for count in (0,4095):
            ctx.sourcemeter.applyVoltage(count*step)
            resp = ctx.tester.runCommand("n")
            print(resp)
            ad_vol.append(resp)
            counter.append(count)
        for count in (4095,0):
            ctx.sourcemeter.applyVoltage(count*step)
            count = count -1
            resp = ctx.tester.runCommand("n")
            print(resp)
            ad_vol.append(resp)
            counter.append(count)
        resp = ctx.tester.runCommand("n")

    # FIXME: no case to return False?
    return True
