
import time
title = "ADC通道遍历2"

desc = '''
    relay k31 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1

    ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)

    loopParam = [
        {"AIN":0, "matrix1":"00000010"}, # GP19
        {"AIN":2, "matrix1":"00100000"}, # GP04
        {"AIN":3, "matrix1":"00010000"}, # GP05
        {"AIN":4, "matrix1":"10000000"}, # GP01
        {"AIN":7, "matrix1":"00001000"}, # GP08
        {"AIN":10, "matrix1":"00000100"}, # GP14
        {"AIN":11, "matrix1":"01000000"}, # GP02
    ]

    for p in loopParam:
        ctx.netmatrix.arrset([p["matrix1"],'00000000','00000000','00000000'])#GP06->SRC case4
        resp = ctx.tester.runCommand("test_adc_chn%d_samp" % (p["AIN"]))
        if resp != 'ready':
            return False

        for vol in [0.5, 1.5]:
            ctx.sourcemeter.applyVoltage(vol)
            resp = ctx.tester.runCommand("next")
            ctx.logger.info("AIN=%d,vol=%f, RESP=%s" % (p["AIN"], vol, resp))

        resp = ctx.tester.runCommand("next")
        if resp != 'end':
            return False

    return True
