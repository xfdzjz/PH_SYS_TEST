import time
title = "pwrMgr4a模块"

desc = '''
    在时钟trim后做此项测试
    稳压源 Channel1 <=> VCC
    源表 <=> GP15
'''


def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.oscilloscope  未使用
    ctx.multimeter 未使用
    '''
    count = []
    vol = []

    # 芯片上电VCC=3V
    ctx.powersupply.voltageOutput(1, 3, 0.1, 3.3, 1)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    # case 3.5.1
    resp = ctx.tester.runCommand("test_pwrMgr4a")
    V1P5A = ctx.sourcemeter.volTest()
    print("VIP5A voltage is %f when VCC is 3v" % (V1P5A))
    ctx.tester.runCommand("next")

    # case 3.5.2
    input("Press ENTER to start VCC = 3V in case 3.5.2")
    ctx.powersupply.voltageOutput(1, 3, 0.1, 3.3, 1)
    V1P5A = ctx.sourcemeter.volTest()
    vol.append(V1P5A)
    count.append(3)
    input("Press ENTER to continue VCC = 5.5V in case 3.5.2")
    ctx.powersupply.voltageOutput(1, 5.5, 0.1, 6, 1)
    V1P5A = ctx.sourcemeter.volTest()
    vol.append(V1P5A)
    count.append(5.5)
    input("Press ENTER to continue VCC = 2.2V in case 3.5.2")
    ctx.powersupply.voltageOutput(1, 2.2, 0.1, 3.3, 1)
    V1P5A = ctx.sourcemeter.volTest()
    vol.append(V1P5A)
    count.append(2.2)

    for (x, y) in zip(count, vol):
        print("VIP5A voltage is %f when VCC is %f" % (y, x))

    resp = ctx.tester.runCommand("next")

    # case 3.5.3
    count = []
    vol = []
    input("Press ENTER to start VCC = 1.5V in case 3.5.3")
    ctx.powersupply.voltageOutput(1, 1.5, 0.1, 3.3, 1)
    ALDO4A = ctx.sourcemeter.volTest()
    vol.append(ALDO4A)
    count.append(1.5)
    ctx.tester.runCommand("next")
    input("Press ENTER to start VCC = 1.55V in case 3.5.3")
    ctx.powersupply.voltageOutput(1, 1.55, 0.1, 3.3, 1)
    ALDO4A = ctx.sourcemeter.volTest()
    vol.append(ALDO4A)
    count.append(1.55)
    ctx.tester.runCommand("next")
    input("Press ENTER to start VCC = 1.60V in case 3.5.3")
    ctx.powersupply.voltageOutput(1, 1.6, 0.1, 3.3, 1)
    ALDO4A = ctx.sourcemeter.volTest()
    vol.append(ALDO4A)
    count.append(1.6)
    ctx.tester.runCommand("next")
    input("Press ENTER to start VCC = 1.7V in case 3.5.3")
    ctx.powersupply.voltageOutput(1, 1.7, 0.1, 3.3, 1)
    ALDO4A = ctx.sourcemeter.volTest()
    vol.append(ALDO4A)
    count.append(1.7)
    ctx.tester.runCommand("next")

    for (x, y) in zip(count, vol):
        print("ALDO4A voltage is %f when VCC is %f v" % (y, x))

    return True
