
title = "cmp反向功能"

desc = '''
    稳压源 Channel1 <=> VCC
    稳压源 Channel2 <=> GP00
    稳压源 Channel3 <=> GP18
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
    ctx.powersupply.voltageOutput(1, 3.3, 0.1, 3.3, 1)
    # dc ps channel2 apply 1.5v to GP00
    ctx.powersupply.voltageOutput(2, 1.5, 0.1, 3.3, 1)
    # dc ps channel3 apply 1.0v to GP18
    ctx.powersupply.voltageOutput(3, 1.0, 0.1, 3.3, 1)

    ctx.tester.runCommand("open_power_en")
    ctx.tester.runCommand("test_model_sel")
    resp = ctx.tester.runCommand("test_cmp_inv")

    while resp != 'end':  # check voltage of souremeter
        print("fail or pass:%s" % (resp))

        if resp == 'pass' or 'fail':
            print("CMP_OUT result is %s" % resp)
        else:
            return False
        resp = ctx.tester.runCommand("next")
    return True
