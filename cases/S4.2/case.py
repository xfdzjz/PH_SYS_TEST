
import time
title = "ADC通道遍历1"

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

    ctx.netmatrix.arrset(['00000001','00000000','00000000','00000000'])
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)

    loopParam = [
        {"AIN":1, "matrix1":"00000001"},
        {"AIN":5, "matrix1":"01000000"},
        {"AIN":6, "matrix1":"00100000"},
        {"AIN":8, "matrix1":"00010000"},
        {"AIN":9, "matrix1":"00001000"},
    ]

    for p in loopParam:
        ctx.netmatrix.arrset([p["matrix1"],'00000000','00000000','00000000'])#GP06->SRC case4
        resp = ctx.tester.runCommand("test_adc_chn%d_samp" % (p["AIN"]))
        if resp != 'ready':
            return False

        for vol in [0.5, 1.5]:
            ctx.sourcemeter.applyVoltage(vol)
            time.sleep(2)
            resp = ctx.tester.runCommand("next")
            ctx.logger.info("AIN=%d,vol=%f, RESP=%s" % (p["AIN"], vol, resp))


        resp = ctx.tester.runCommand("next",1)
        if resp != 'end':
            return False

    return True
