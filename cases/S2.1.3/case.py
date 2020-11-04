
import time
title = "HRC随VCC变化"

desc = '''
relay k15 connect
'''


def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    times = 0.000001
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(
        ['00000000', '00000000', '00010000', '00000000'])  # GP14->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    count = 0
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("HRCTestOnVCCVerify", 3)
    ctx.oscilloscope.timeset(times)#示波器x轴一格多宽
    # scale = [0.000001, 0.000001, 0.000001, 0.000001, 0.000001]

    scale = [0.000001, 0.0000002, 0.0000002, 0.0000001, 0.00000005]
    while resp != 'end':
        if resp[0:3] == 'hrc':
            for vcc in [3.3, 5, 2.2]:
                ctx.powersupply.voltageOutput(3, vcc, 0.1, 6, 1)
                ctx.oscilloscope.inst.write(":TIMebase:MAIN:SCALe %1.8f" %scale[count])
                ctx.oscilloscope.inst.write(":RUN")
                time.sleep(0.1)
                ctx.oscilloscope.inst.write(":STOP")
                time.sleep(1)
                duty, fre = ctx.oscilloscope.paraTest(2)
                ctx.logger.info("VCC is %1.1fv fre is %f, duty is %f" % (vcc, fre/1000000, duty))
            count = count + 1
        else:
            return False
        resp = ctx.tester.runCommand("next", 1)

    return True
