import time
title = "ADC参考电压遍历"

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
    #ctx.powersupply.voltageOutput(1, 3, 0.1, 5, 1)
    ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])#GP04->src GP14->vref
    ctx.sourcemeter.applyVoltage(3.3)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_int_vref")
    count = 0

    while resp !="end":
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
        resp = ctx.tester.runCommand("n")



    for (x,y) in (ad_vol,counter):
        print("case %d voltage is %f"%(y,x))


    return True
