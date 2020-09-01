
import time
title = "HRC自动trim流程"

desc = '''
relay has no connection
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=3
    fre = 1
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.netmatrix.relayset(['00000000','00000000','00000000','00000000'])


    resp = ctx.tester.runCommand("TestHrcTrim")
    while resp != 'end':
        if resp != 'fail':
            with open("nvrdata.txt","a") as f:
                f.write(resp[7:]+' '+str(fre)+'M'+'\n')
                fre = fre*2
        else:
            with open("nvrdata.txt","a") as f:
                f.write("case 1.4 fail ")
            return False
        resp = ctx.tester.runCommand("next")
    return True
