import time
title = "ADC参考电压遍历"

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
    --- test_adc_int_vref -->
    <-- 1200mv ---
    --- n -->       调整电压，发送n
    <--- XXX ---    返回采样值，上两步循环4096 * 2 次, 
    --- n -->       
    <-- 1500mv ---
    --- n -->       调整电压，发送n
    <--- XXX ---    返回采样值，上两步循环4096 * 2 次, 
    --- n -->
    <-- 2000mv ---
    --- n -->       调整电压，发送n
    <--- XXX ---    返回采样值，上两步循环4096 * 2 次, 
    --- n -->
    <-- 2500mv ---
    --- n -->       调整电压，发送n
    <--- XXX ---    返回采样值，上两步循环4096 * 2 次, 
    --- n -->
    <-- end ---
    '''
    # 芯片上电VCC=3V
    ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])#GP04->src GP14->vref
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")

    mv = ctx.tester.runCommand("test_adc_int_vref")

    for i in range(0,4):
        ret = adcLoop(ctx,mv)
        if not ret :
            return False
        mv = ctx.tester.runCommand("n")
    # last mv shall be 'end'

    mv = ctx.tester.runCommand("test_adc_ext_vref")
    ret = adcLoop(ctx,mv)
    if not ret :
        return False
    mv = ctx.tester.runCommand("n")
    # last mv shall be 'end'

    mv = ctx.tester.runCommand("test_adc_ext_vcc")
    ret = adcLoop(ctx,mv)
    if not ret :
        return False
    mv = ctx.tester.runCommand("n")
    # last mv shall be 'end'

    return True
