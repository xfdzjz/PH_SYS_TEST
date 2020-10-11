
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
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(
        ['00000000', '00000000', '00010000', '00000000'])  # GP14->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
<<<<<<< HEAD
    time.sleep(0.50)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("HRCTestOnVCCVerify", 3)

    while resp != 'end':
=======
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("HRCTestOnVCCVerify")

    while resp !='end':
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
        if resp[0:3] == 'hrc':
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
<<<<<<< HEAD
            ctx.logger.info("VCC is 3.3v fre is %f, duty is %f" % (fre, duty))
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 6, 1)
            time.sleep(1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            ctx.logger.info("VCC is 2.2v fre is %f, duty is %f" % (fre, duty))
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            time.sleep(1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            ctx.logger.info("VCC is 5v fre is %f, duty is %f" % (fre, duty))
=======
            ctx.logger.info("VCC is 3.3v fre is %f, duty is %f" %(fre,duty))
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            ctx.logger.info("VCC is 5v fre is %f, duty is %f" %(fre,duty))
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            para = ctx.oscilloscope.paraTest(2)
            fre = para[1]
            duty = para[0]
            ctx.logger.info("VCC is 2.2v fre is %f, duty is %f" %(fre,duty))
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
            ctx.powersupply.voltageOutput(3, 3.3, 0.1, 6, 1)
        else:
            return False
        resp = ctx.tester.runCommand("next", 3)

    return True
