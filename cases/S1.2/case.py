
import time
title = "BGS自动trim流程"

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
    ctx.netmatrix.arrset(['00000000','00001000','00000000','00000000'])#ps4->gp15 1.21v
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(250)
    ctx.powersupply.voltageOutput(4, 1.21, 0.1, 3.3, 1)
    resp = ctx.tester.runCommand("TestBGSTrim")
<<<<<<< HEAD

    if resp != 'fail':
        print(resp)
    else:
=======
    print(resp)
    if resp == 'fail':
>>>>>>> 3726e50be1b4c95cf2cd829665a94fe7071e50f6
        return False

    counter = 1
    target = 2

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
    ctx.powersupply.voltageOutput(4, 0, 0.1, 3.3, 1)
    return True

