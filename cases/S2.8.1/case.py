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
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_freq")
    count = 0

    while resp !="end":
        print(resp)
        if resp[-2:] == 'mv':
            vol = float(resp[:-2])
            step = vol / 4096
        for count in (0,4096):
            ctx.sourcemeter.applyVoltage(count*step)
            resp = ctx.tester.runCommand("n")
            print(resp)
            ad_vol.append(resp)
            counter.append(count)
        for count in (4096,0):
            ctx.sourcemeter.applyVoltage(count*step)
            count = count -1
            resp = ctx.tester.runCommand("n")
            print(resp)
            ad_vol.append(resp)
            counter.append(count)
        count = count + 1
        resp = ctx.tester.runCommand("n")
        if count == 1 :
            ctx.powersupply.voltageOutput(3, 5.0, 0.1, 6, 1)
        if count == 2 :
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
    return True
