
import time
title = "VDD稳定性测试"

desc = '''
    在时钟trim后做此项测试
    稳压源 Channel3 <=> VCC
    源表  <=> VBGS
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.oscilloscope.trig(2,'POS',2.5)
    ctx.netmatrix.arrset(['00000010','00000010','00000100','00000000'])#VCC->SRC
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.sourcemeter.applyVoltage(3)
    time.sleep(1)

    ctx.sourcemeter.applyVoltage(0)

    ctx.oscilloscope.trig(2,'POS',0.1)
    ctx.sourcemeter.rampvol(0,3,1,0.033)

    vol = ctx.oscilloscope.readRamData(2,2,1,15625)

    print(vol)

    return True
