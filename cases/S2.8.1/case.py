import time
title = "ADC采样速率遍历4MHz~500KHz"

desc = '''
    relay k5,k14 connect
'''

def adcLoop(ctx, mv):
    if mv[-2:] != 'mv':
        return False
    step = float(mv[:-2]) / 4096
    for i in (0,4096):
        ctx.sourcemeter.applyVoltage(i*step)
        adcHex = ctx.tester.runCommand("n")
        print(adcHex)
    for i in (4095,-1,-1):
        ctx.sourcemeter.applyVoltage(i*step)
        adcHex = ctx.tester.runCommand("n")
        print(adcHex)
    return True

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    PC          PHNX
    --- test_adc_freq -->
    <-- ready ---
    --- next -->
    <-- 2500mv ---
    --- n -->       调整电压，发送n
    <--- XXX ---    返回采样值，上两步循环4096 * 2 * 7次, 
    --- n -->
    <-- end ---
    '''
    # 芯片上电VCC=3V
    #ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])#GP04->src GP14->vref
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_freq")
    if resp != "ready":
        return False

    step = 0.0
    stage = 0

    mv = ctx.tester.runCommand("next")
    for i in range(0,7):
        ret = adcLoop(ctx, mv)
        if ret == False:
            return False
        if i == 5 :
            ctx.powersupply.voltageOutput(3, 5.0, 0.1, 6, 1)
        elif i == 6 :
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
        else:
            pass
        mv = ctx.tester.runCommand("n")

    # last mv shall be 'end'
    return True
