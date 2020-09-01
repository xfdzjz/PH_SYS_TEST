
import time
title = "CMP自动校准"

desc = '''
relay has no connection
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1

    ctx.netmatrix.arrset(['00000000','00000000','00000000','00000000'])
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    resp = ctx.tester.runCommand("TestCmpTrim")
    print(resp)

    if resp != 'fail':
        print(resp)
    else:
        with open("nvrdata.txt","a") as f:
            f.write("case 1.1 fail ")
        return False
    with open("nvrdata.txt","a") as f:
        f.write(resp[7:]+'\n')
    return True
