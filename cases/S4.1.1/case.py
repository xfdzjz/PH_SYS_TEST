
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
    ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)#v1
    ctx.powersupply.voltageOutput(2, 1.5, 0.1, 3.3, 1)# v2 dc ps channel2 apply 1.5v to VC1N0/VC1N1/VC1P0-VC1P5


    ctx.tester.runCommand("open_power_en")
    ctx.tester.runCommand("test_mode_sel")
    resp = ctx.tester.runCommand("test_cmp_chn")

    if resp != 'ready':
        return False
    while resp != 'end':#check voltage of souremeter
        print("fail or pass:%s" % (resp))

        if resp == 'pass' and  counter ==0 :
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)#v1
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
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])#GP00,11->vref1,2 case4
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
        elif  resp == 'pass' and counter ==3 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==4 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==5 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==6 :
            ctx.netmatrix.arrset(['0000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==7 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==8 :
            ctx.netmatrix.arrset(['0000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==9 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==10 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==11 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==12 :
            ctx.netmatrix.arrset(['0000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==13 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==14 :
            ctx.netmatrix.arrset(['0000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==15 :
            ctx.netmatrix.arrset(['00000000','10000000','00000000','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==16 :
            ctx.netmatrix.arrset(['00000000','10000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1.5, 0.1, 3.3, 1)
            ctx.powersupply.voltageOutput(2, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==17 :
            ctx.netmatrix.arrset(['00000000','10000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(2, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==18 :
            ctx.netmatrix.arrset(['00000000','00000010','00000001','00000000'])
            ctx.powersupply.voltageOutput(2, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==19 :
            ctx.netmatrix.arrset(['00000000','00000010','00000001','00000000'])
            ctx.powersupply.voltageOutput(2, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==20 :
            ctx.netmatrix.arrset(['00000000','01000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==21 :
            ctx.netmatrix.arrset(['00000000','01000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==22 :
            ctx.netmatrix.arrset(['0000000','00100000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==23 :
            ctx.netmatrix.arrset(['0000000','00100000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==24 :
            ctx.netmatrix.arrset(['00000000','00010000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==25 :
            ctx.netmatrix.arrset(['00000000','00010000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==26 :
            ctx.netmatrix.arrset(['0000000','00000100','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif resp == 'pass' and counter ==27 :
            ctx.netmatrix.arrset(['0000000','00000100','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==28 :
            ctx.netmatrix.arrset(['00000000','00000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==29 :
            ctx.netmatrix.arrset(['00000000','00000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==30 :
            ctx.netmatrix.arrset(['00000000','00000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 2.5, 0.1, 3.3, 1)
            counter = counter + 1
        elif  resp == 'pass' and counter ==31 :
            ctx.netmatrix.arrset(['00000000','00000000','00000001','00000000'])
            ctx.powersupply.voltageOutput(4, 1, 0.1, 3.3, 1)
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
