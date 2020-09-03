
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
    time.sleep(0.250)
    resp = ctx.tester.runCommand("EnterEstMode")
    if resp != 'pass':
        return False
    resp = ctx.tester.runCommand("TestCmpTrim")
    resp = ctx.tester.runCommand(PrgWordToNVR0)
    target_vol = resp
    vol_len =  len(target_vol)

    print(resp)
    counter = 1
    target = 1
    if resp != 'fail':
        print(resp)
    else:
        return False
    with open("nvr.json","r") as f:
        data = f.read()
        for i in ranger (0,len(data)):
            if data[i] == ':' and target == counter:
                data = data.replace(data[i-6:i+2],data[i-6:i+1]+target_vol,1)
                target = 0
            elif data[i] == ':' and target != counter:
                counter = counter +1
        f.write(data)
        f.close()
    return True
