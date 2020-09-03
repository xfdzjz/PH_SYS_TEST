
title = "cmp反向功能"

desc = '''
    relay k1 and k22 connect
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
    ctx.netmatrix.arrset(['10000000','00000100','00000000','00000000'])#GP00->src GP18->vref
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(250)
    ctx.powersupply.voltageOutput(4, 1.5, 0.1, 3.3, 1)# dc ps channel4 apply 1.5v to GP00
    ctx.powersupply.voltageOutput(2, 1.0, 0.1, 3.3, 1)# dc ps channel2 apply 1.0v to GP18

    ctx.tester.runCommand("open_power_en")
    ctx.tester.runCommand("test_mode_sel")
    resp = ctx.tester.runCommand("test_cmp_inv")

    while resp  != 'end':#check voltage of souremeter
        print("fail or pass:%s" % (resp))

        if resp == 'pass' or 'fail':
            print("CMP_OUT result is %s"%resp)
        else :
            return False
        resp = ctx.tester.runCommand("next")
    return True
