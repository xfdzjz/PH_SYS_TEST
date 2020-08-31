
title = "CMP迟滞功能"

desc = '''
    在时钟trim后做此项测试
    稳压源 Channel1 <=> VCC
    稳压源 Channel2 <=> GP18
    源表 <=> GP00
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    #ctx.oscilloscope.prepareChannel(3, 1000, 300)
    #ctx.oscilloscope.getWave(3, 1000, 300)


    # 芯片上电VCC=3V
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    gp00vol = 1.2

    ctx.powersupply.voltageOutput(4, 1.2, 0.1, 3.3, 1)# dc ps channel4 apply 1.2v to GP18
    ctx.sourcemeter.applyVoltage(gp00vol) # sourcemeter apply 1.2v to GP00
    ctx.netmatrix.arrset(['00000000','00000000','00001000','00000000'])#GP15->OSC
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_cmp_hys")

    while resp != 'end':#check voltage of souremeter
        print("GP00=%f resp: %s" % (gp00vol, resp))

        if resp == '1mv+':
            gp00vol = gp00vol + 0.001
            ctx.sourcemeter.applyVoltage(gp00vol)
        elif resp == '1mv-':
            gp00vol = gp00vol - 0.001
            ctx.sourcemeter.applyVoltage(gp00vol)
        elif resp[:6] == 'result':
            # showing the result voltage of abs(V1-V0)
            print("vol diff is %s mv" %resp[-2:])
        else:
            return False
        resp = ctx.tester.runCommand("next")
    return True
