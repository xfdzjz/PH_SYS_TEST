import time
title = "DCDC VOOK功能"

desc = '''
    源表 <=> PDAS
    稳压源channel2 <=> VCC
    示波器 <=> GP15(VO1)
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.powersupply 使用
    ctx.multimeter  使用
        '''

    vol = 3

    # 芯片上电VCC=3V
    ctx.powersupply.voltageOutput(1, 3.3, 0.1, 4, 1)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_bzdrv_step_bz")
    while resp !='end':
        if resp == "ready1":
            para = ctx.oscilloscope.paraTest(1)#horns、hornb、fi
            duty1 = para[0]
            print("horn duty1 is %f, period is %f" %(duty1,1/para[1]))
            para = ctx.oscilloscope.paraTest(2)#horns、hornb、fi
            duty1 = para[0]
            print("hornb duty1 is %f, period is %f" %(duty1,1/para[1]))
            para = ctx.oscilloscope.paraTest(1)#horns、hornb、fi
            duty2 = para[0]
            print("horn duty2 is %f" %duty2)
            para = ctx.oscilloscope.paraTest(2)#horns、hornb、fi
            duty2 = para[0]
            print("hornb duty2 is %f" %duty2)


            resp = ctx.tester.runCommand("next")

        elif resp == "ready2":

            para = ctx.oscilloscope.paraTest(1)#horns、hornb、fi
            duty = para[0]
            if duty < 0.55 and duty > 0.45:
                print("pass horn duty is %f" %duty)
            else:
                print("fail horn duty is %f" %duty)
            para = ctx.oscilloscope.paraTest(2)#horns、hornb、fi
            duty = para[0]
            if duty < 0.55 and duty > 0.45:
                print("pass hornb duty is %f" %duty)
            else:
                print("fail hornb duty is %f" %duty)
            para = ctx.oscilloscope.paraTest(3)#horns、hornb、fi
            duty = para[0]
            if duty < 0.55 and duty > 0.45:
                print("pass fi duty is %f" %duty)
            else:
                print("fail fi duty is %f" %duty)
            resp = ctx.tester.runCommand("next")

        else:
            return False



    return True
