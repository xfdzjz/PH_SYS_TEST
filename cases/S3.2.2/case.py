
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
    ctx.sourcemeter.applyVoltage(0)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.oscilloscope.trigMul(2,'POS',0.7,scale = 0.05)
    ctx.oscilloscope.trigMul(1,'POS',1.5,scale = 0.05)
    time.sleep(1)

    ctx.sourcemeter.applyVoltage(0)
    ctx.sourcemeter.applyVoltage(3)

    vol = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
    vol1 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
    print(vol)#vcc
    print(vol1)#por
    input('n')
    ctx.sourcemeter.applyVoltage(0)

    ctx.oscilloscope.trigMul(2,'POS',0.7,scale = 0.05)
    #ctx.oscilloscope.trigSlope(1,"PGReater",0.1,1.5,0.1)


    ctx.sourcemeter.rampvol(0,3.1, 0.033,1)#(start,target,de,steps): 33ms->上升1v

    vol2 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
    vol3 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')

    print(vol2)
    print(vol3)
    input('n')

    count = 0
    counter = 0
    for i in range(0,len(vol)):
        if float(vol[i])>=2.9 :
            count = i
            break

    for j in range(0,len(vol)):
        if float(vol1[j]) >=1.45:
            counter = j
            break
    timeDiff = ctx.oscilloscope.xincre()
    diff = timeDiff*(count - counter)
    ctx.logger.info("hurry time is %s"%diff)


    count = 0
    counter = 0

    for i in range(0,len(vol2)):
        if float(vol2[i])>=1.5 and count ==0:
            count = i
            break

    for j in range(0,len(vol3)):
        if float(vol3[j])>=0.1 and counter ==0:
            counter = j
            break
    diff = timeDiff*(count - counter)
    ctx.logger.info("slow time is %s"%diff)

    return True
