
import time
title = "POR功能"

desc = '''
     relay k25,K23 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00000010','00000000','00000100','00000000'])#VCC->src por->osc2
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.oscilloscope.trig(2,'POS',2.5)
    ctx.sourcemeter.rampvol(0,3.3,1,1)
    time.sleep(1)
    ctx.oscilloscope.trig(2,'NEG',0.1)
    ctx.sourcemeter.rampvol(3.3,0,1,1)

    vol = ctx.oscilloscope.readRamData(2,2,1,15625)

    print(vol)

    return True
