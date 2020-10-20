
import time
title = "BZ导通压降"

desc = '''
relay k5, k9 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])#HORNS->SRC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.powersupply.voltageOutput(2, 10.5, 0.1, 3.3, 1)#vh
    ctx.powersupply.voltageOutput(4, 0, 0.1, 3.3, 1)#FI
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("bzOnVoltDrop",3)
    ctx.logger.info(resp)
    if resp != 'ready':
        return False

    ctx.sourcemeter.applyVoltage(0.5)#源表给电压
    amp = ctx.sourcemeter.ampTest() * 1000 #源表测电流
    ctx.logger.info("I_BZNS amp is %f mA when sourmeter is 0.5v"%amp)
    ctx.sourcemeter.applyVoltage(0.0)#源表给电压
    resp = ctx.tester.runCommand("next")
    if resp != 'ready':
        return False

    ctx.sourcemeter.channel('off')
    ctx.netmatrix.arrset(['00100000','00000000','00000000','00000000'])#HORNB->SRC
    i,v = ctx.sourcemeter.ivTest()
    print(i,v)
    input("n")
    # ctx.sourcemeter.applyVol(10)
    ctx.sourcemeter.channel('on')
    time.sleep(3)
    amp = ctx.sourcemeter.ampTest() * 1000
    ctx.logger.info("I_BZPB amp is %f mA when sourmeter is 10v"%amp)
    ctx.sourcemeter.applyVol(0)
    resp = ctx.tester.runCommand("next")
    if resp != 'ready':
        return False

    ctx.powersupply.voltageOutput(4, 10.5, 0.1, 12, 1)
    input("n")
    ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])#HORNS->SRC
    ctx.sourcemeter.applyVol(10)
    amp = ctx.sourcemeter.ampTest() * 1000
    ctx.logger.info("I_BZPS amp is %f mA when sourmeter is 10v"%amp)
    resp = ctx.tester.runCommand("next")
    if resp != 'ready':
        return False
    input("n")

    ctx.sourcemeter.channel('off')
    time.sleep(2)
    ctx.netmatrix.arrset(['00100000','00000000','00000000','00000000'])#HORNB->SRC
    ctx.sourcemeter.applyVoltage(0.5)
    ctx.sourcemeter.channel('on')
    time.sleep(3)
    amp = ctx.sourcemeter.ampTest() * 1000
    ctx.logger.info("I_BZNB amp is %f mA when sourmeter is 0.5v"%amp)
    resp = ctx.tester.runCommand("next")
    if resp!= 'end':
        return False

    return True
