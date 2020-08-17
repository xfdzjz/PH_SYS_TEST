
title = "cmp通道选择"

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
    ctx.powersupply.voltageOutput(1, 2.5, 0.1, 3.3, 1)
    # dc ps channel2 apply 1.5v to VC1N0/VC1N1/VC1P0-VC1P5
    ctx.powersupply.voltageOutput(2, 1.5, 0.1, 3.3, 1)

    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_cmp_chn")
    ctx.tester.runCommand("test_model_sel")

    while resp != 'end':  # check voltage of souremeter
        print("fail or pass:%s" % (resp))

        if resp == 'pass':
            ctx.powersupply.voltageOutput(1, 2.5, 0.1, 3.3, 1)
            count.append(counter)
            PassOrFail.append(resp)
            counter = counter + 1
        elif resp == 'fail':
            ctx.powersupply.voltageOutput(1, 1, 0.1, 3.3, 1)
            count.append(counter)
            PassOrFail.append(resp)
            counter = counter + 1

        input("Press ENTER to continue")
        resp = ctx.tester.runCommand("next")

    for (x, y) in zip(count, PassOrFail):
        if x <= 5:
            print("VC1N%d is %s" % (x, y))
        elif x <= 12:
            print("VC1P%d is %s" % (x-6, y))
        else:
            break

    return True
