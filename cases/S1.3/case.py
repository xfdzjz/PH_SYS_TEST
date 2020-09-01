
import time
title = "BGA自动trim流程"

desc = '''
relay k18 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.relayset(['00000000','00001000','00000000','00000000'])#ps4->gp15 1.21v
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.powersupply.voltageOutput(4, 1.22, 0.1, 3.3, 1)
    resp = ctx.tester.runCommand("TestBGATrim")
    print(resp)

    if resp != 'fail':
        print(resp)
    else:
        with open("nvrdata.txt","a") as f:
            f.write("case 1.5 fail ")
        return False
    with open("nvrdata.txt","a") as f:
        f.write(resp[7:]+'\n')

    ctx.powersupply.voltageOutput(4, 0, 0.1, 3.3, 1)
    return True
