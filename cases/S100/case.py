
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
    ctx.powersupply.voltageOutput(1, 5.5, 0.1, 6, 1)
    #a = ctx.sourcemeter.readbit(4)
    #if a =='ok':
    #    ctx.sourcemeter.pulseAmp( 0, 10E-10, 10E-5)
    return True
