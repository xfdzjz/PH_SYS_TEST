
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
    ctx.sourmeter.applyVoltage(3.3)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.oscilloscope.trig(2,'POS',2.5)
    ctx.sourcemeter.rampvol(0,3.3,1,1)
    if ctx.oscilloscope.statusCheck() == False:
        return False
    time.sleep(1)
    ctx.oscilloscope.trig(2,'NEG',0.1)
    ctx.sourcemeter.rampvol(3.3,0,1,1)

    vol = ctx.oscilloscope.readRamData(2,2,1,15625)
    for i in range(0,len(vol)):
        if vol[i+1]- vol[i] >=0.2:
            print("VTR is (low->hig) %s" %vol[i+1])
        if vol[i]- vol[i+1] >=0.2:
            print("VTR is (hig->low) %s" %vol[i+1])

    if ctx.oscilloscope.statusCheck() == False:
        return False
    return True
