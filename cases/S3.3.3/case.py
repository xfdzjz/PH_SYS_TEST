
import time
title = "LEDDRV电流值"

desc = '''
relay k13,k17 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00001000','00000000','00000000','00000000'])#BLED->SRC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)#vcc
    ctx.powersupply.voltageOutput(2, 5.7, 0.1, 7, 1)#vh
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("ledDrive",3)

    if resp != 'ready':
        return False
    # ctx.powersupply.voltageOutput(1, 2, 0.2, 7, 0.2)#给电压
    # amp = ctx.powersupply.measure(1,'CURRent') * 1000 #测电流
    ctx.sourcemeter.applyVoltage(2)
    amp = ctx.sourcemeter.ampTest() * 1000
    # amp =0
    ctx.logger.info("Ibled amp is %f mA when VCC is 3.3v"%amp)
    # ctx.powersupply.channelOff(1)
    ctx.netmatrix.arrset(['00000000','00000000','00000000','00000000'])#BLED->SRC
    resp = ctx.tester.runCommand("next",2)
    # ctx.powersupply.channelOn(1)
    ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#BLED->SRC
    # ctx.powersupply.voltageOutput(1, 2, 0.2, 7, 0.2)
    ctx.sourcemeter.applyVoltage(2)
    amp = ctx.sourcemeter.ampTest() * 1000
    # amp = ctx.powersupply.measure(1,'CURRent') * 1000
    ctx.logger.info("Irbled amp is %f mA when VCC is 3.3v"%amp)
    resp = ctx.tester.runCommand("next",2)
    if resp != 'end':
        return False
    return True
