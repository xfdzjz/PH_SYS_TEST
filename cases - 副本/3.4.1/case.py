import time
title = "pwrMgr模块"

desc = '''
    稳压源 Channel2 <=> VCC
    源表 <=> V1P5S/V1P5D
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''
    count = []

    vol = []


    # 芯片上电VCC=3V
    ctx.powersupply.voltageOutput(2, 3, 0.1, 3.3, 1)
    ctx.tester.runCommand("open_power_en")
    ctx.tester.runCommand("test_mode_sel")

    #case 3.4.1
    resp = ctx.tester.runCommand("test_pwrMgr")
    time.sleep(0.1)
    V1P5 = ctx.sourcemeter.volTest()
    print("GP15 vol is %f mv" %V1P5)
    resp = ctx.tester.runCommand("next")

    #case 3.4.2
    input("Press ENTER to start case 3.4.2 (VCC = 3V)")
    ctx.powersupply.voltageOutput(2, 3, 0.1, 3.3, 1)
    V1P5 = ctx.sourcemeter.volTest()
    vol.append(V1P5)
    count.append(3)
    input("Press ENTER to continue case 3.4.2 (VCC = 5.5V)")
    ctx.powersupply.voltageOutput(2, 5.5, 0.1, 6, 1)
    V1P5 = ctx.sourcemeter.volTest()
    vol.append(V1P5)
    count.append(5.5)
    input("Press ENTER to continue case 3.4.2 (VCC = 2.2V)")
    ctx.powersupply.voltageOutput(2, 2.2, 0.1, 3.3, 1)
    V1P5 = ctx.sourcemeter.volTest()
    vol.append(V1P5)
    count.append(2.2)

    for (x,y) in zip(count,vol):
        print("VIP5 voltage is %f when VCC is %f"%(y,x))

    #case 3.4.3
    input("Press ENTER to continue case 3.4.3 (VCC vovl= 3V)")
    ctx.powersupply.voltageOutput(2, 3, 0.1, 3.3, 1)
    V1P5 = ctx.sourcemeter.volTest()
    print("VIP5 voltage is %f when SLDO output vol is 1.2V "%(V1P5))




    return True
