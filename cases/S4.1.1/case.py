import time
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


<<<<<<< HEAD
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.tester.runCommand("test_mode_sel",0.2)
=======
    ctx.tester.runCommand("open_power_en")
    #ctx.tester.runCommand("test_mode_sel")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    resp = ctx.tester.runCommand("test_cmp_chn")

    if resp != 'ready':
        return False

    params = [
        ['10000000', '00000001', 2.5, 1.5 ], #GP00,18
        ['10000000', '00000001', 1.0, 1.5 ], #GP00,18
        ['10000000', '00001000', 2.5, 1.5 ], #GP00,11
        ['10000000', '00001000', 1.0, 1.5 ], #GP00,11
        ['10000000', '00000000', 2.5, 1.5 ], #GP00,int
        ['10000000', '00000000', 1.0, 1.5 ], #GP00,int
        ['10000000', '00000000', 2.5, 1.5 ], #GP00,int
        ['10000000', '00000000', 1.0, 1.5 ], #GP00,int
        ['10000000', '00000000', 2.5, 1.5 ], #GP00,int
        ['10000000', '00000000', 1.0, 1.5 ], #GP00,int
        ['10000000', '00000000', 2.5, 1.5 ], #GP00,int
        ['10000000', '00000000', 1.0, 1.5 ], #GP00,int
        ['10000000', '00000000', 2.5, 1.5 ], #GP00,int
        ['10000000', '00000000', 1.0, 1.5 ], #GP00,int
        ['10000000', '00000000', 2.5, 1.5 ], #GP00,int
        ['10000000', '00000000', 1.0, 1.5 ], #GP00,int
        ['10000000', '00000001', 1.5, 2.5 ], #GP00,18
        ['10000000', '00000001', 1.5, 1.0 ], #GP00,18
        ['00000010', '00000001', 1.5, 2.5 ], #GP15,18
        ['00000010', '00000001', 1.5, 1.0 ], #GP15,18
        ['01000000', '00000001', 1.5, 2.5 ], #GP06,18
        ['01000000', '00000001', 1.5, 1.0 ], #GP06,18
        ['00100000', '00000001', 1.5, 2.5 ], #GP07,18
        ['00100000', '00000001', 1.5, 1.0 ], #GP07,18
        ['00010000', '00000001', 1.5, 2.5 ], #GP10,18
        ['00010000', '00000001', 1.5, 1.0 ], #GP10,18
        ['00000100', '00000001', 1.5, 2.5 ], #GP13,18
        ['00000100', '00000001', 1.5, 1.0 ], #GP13,18
        ['00000000', '00000001', 1.5, 2.5 ],
        ['00000000', '00000001', 1.5, 1.0 ],
        ['00000000', '00000001', 1.5, 2.5 ],
        ['00000000', '00000001', 1.5, 1.0 ]
    ]

    for i in range(0,len(params)):
        ctx.netmatrix.arrset(['00000000',params[i][0],params[i][1],'00000000'])
        ctx.powersupply.voltageOutput(4, params[i][3], 0.1, 3.3, 1)#v2
        ctx.powersupply.voltageOutput(2, params[i][2], 0.1, 3.3, 1)#v1
<<<<<<< HEAD
        resp = ctx.tester.runCommand("next",2)
=======
        resp = ctx.tester.runCommand("next")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
        PassOrFail.append(resp)

    ctx.logger.info(PassOrFail)
    ctx.logger.debug(PassOrFail)
    if PassOrFail[-1]  != 'end':
        return False


    return True
