
import time
title = "POR延时"

desc = '''
relay k25,k26,k23 connect
'''
filename = '3.2.2data.txt'

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00000010','00000000','00000100','00000010'])#VCC->src,osc1 POR->osc2
    ctx.sourcemeter.applyVoltage(3.3)
    time.sleep(0.250)
    #ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.oscilloscope.trig(2,'POS',0.7)
    ctx.oscilloscope.trigMul(1,'POS',1.5,scale = 0.01)
    time.sleep(3)
    ctx.sourcemeter.applyVoltage(0)
    ctx.sourcemeter.applyVoltage(3)
    vol = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
    vol1 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')

    ctx.sourcemeter.applyVoltage(0)

    ctx.oscilloscope.trigMul(2,'POS',1.5,scale = 0.01)
    ctx.oscilloscope.trigSlope(1,"PGReater",0.1,1.5)
    time.sleep(3)

    ctx.sourcemeter.rampvol(0,3.0, -1,1)
    vol2 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
    vol3 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')

    with open(filename,"w") as f:
        f.write("osc1 data: \n")
        f.write(str(vol1))
        f.write("\n")
        f.write("osc2 data: \n")
        f.write(str(vol))
        f.write("osc1 data: \n")
        f.write(str(vol3))
        f.write("\n")
        f.write("osc2 data: \n")
        f.write(str(vol2))
    count = 0
    counter = 0
    for i in range(0,len(vol)):
        if float(vol[i])>=1.5 and count ==0:
            count = i

    for j in range(0,len(vol)):
        if float(vol1[j]) >=0.1 and counter == 0:
            counter = j
    timeDiff = ctx.oscilloscope.xincre()

    diff = timeDiff*(count - counter)
    ctx.logger.info("diff time is %f" %diff)
    count = 0
    counter = 0
    for i in range(0,len(vol)):
        if float(vol2[i])>=1.5 and count ==0:
            count = i

    for j in range(0,len(vol)):
        if float(vol3[j]) >=0.1 and counter == 0:
            counter = j
    diff = timeDiff*(count - counter)
     ctx.logger.info("diff time is %f" %diff)

    return True
