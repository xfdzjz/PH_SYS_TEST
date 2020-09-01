
import time
title = "MRC自动trim流程"

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
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    ctx.netmatrix.relayset(['00000000','00000000','00000000','00000000'])

    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("TestMRCTrim")
    if resp != 'fail':
        print(resp)
    else:
        with open("nvrdata.txt","ab") as f:
            f.write("case 1.6 fail ")
        return False


    with open("nvrdata.txt","ab") as f:
        f.write(resp[7:]+'\n')
    return True

