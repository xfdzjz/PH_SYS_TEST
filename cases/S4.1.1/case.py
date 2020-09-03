
title = "CMP通道遍历"

desc = '''
    稳压源 Channel1 <=> VC1P0/VC1N0
    稳压源 Channel2 <=> VC1N0/VC1N1/VC1P0-VC1P5
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''
    count = []
    counter = 0
    PassOrFail = []

    # 芯片上电VCC=3V
    ctx.netmatrix.arrset(['00000000','10000000','00000001','00000000'])#GP00,18->vref1,2 case4
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(0.250)
    ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
    ctx.powersupply.voltageOutput(2, 1.5, 0.1, 3.3, 1)# dc ps channel2 apply 1.5v to VC1N0/VC1N1/VC1P0-VC1P5


    ctx.tester.runCommand("open_power_en")
    ctx.tester.runCommand("test_mode_sel")
    resp = ctx.tester.runCommand("test_cmp_chn")


    while resp != 'end':#check voltage of souremeter
        print("fail or pass:%s" % (resp))

        if resp == 'pass' and  counter ==0 :
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            count.append(counter)
            PassOrFail.append(resp)
            counter = counter + 1
        elif resp == 'pass' and  counter ==1 :
            ctx.netmatrix.arrset(['00000000','10000000','00001000','00000000'])#GP00,11->vref1,2 case4
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            count.append(counter)
            PassOrFail.append(resp)
            counter = counter + 1
        elif resp == 'pass' and  counter ==2 :
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            count.append(counter)
            PassOrFail.append(resp)
            counter = counter + 1
            ctx.netmatrix.arrset(['00000000','10000000','00001000','00000000'])#GP00,11->vref1,2 case4
        elif  resp == 'pass' and counter ==3 :
            ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])
            counter = counter + 1
        elif  resp == 'pass' and counter ==4 :
            ctx.netmatrix.arrset(['01000000','00000000','00000000','00000000'])
            counter = counter + 1
        elif resp == 'pass' and counter ==5 :
            ctx.netmatrix.arrset(['00100000','00000000','00000000','00000000'])
            counter = counter + 1
        elif resp == 'pass' and counter ==6 :
            ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])
            counter = counter + 1
        elif resp == 'pass' and counter ==7 :
            ctx.netmatrix.arrset(['00000100','00000000','00000000','00000000'])
            counter = counter + 1
        elif resp == 'fail':
            ctx.powersupply.voltageOutput(1, 1, 0.1, 3.3, 1)
            count.append(counter)
            PassOrFail.append(resp)
            counter = counter + 1
        resp = ctx.tester.runCommand("next")

    for (x,y) in zip(count, PassOrFail):
        if x <= 5 :
            print("VC1N%d is %s"%(x, y))
        elif x <= 12 :
            print("VC1P%d is %s"%(x-6, y))
        else:
            break

    return True
