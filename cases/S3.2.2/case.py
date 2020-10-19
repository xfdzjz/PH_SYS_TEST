
import time
title = "POR延时"

desc = '''
relay k25,k26,k23 connect
'''
filename = '3.2.2data.txt'

def calcDelay(xincre, vccWave, porWave, vccThrld, porThrld):
    vccPos = -1
    porPos = -1
    if len(vccWave) <= 1 or len(porWave) <= 1:
        return False, 0
    for i in range(0,len(vccWave)):
        vcc = float(vccWave[i])
        if vcc>=vccThrld :
            vccPos = i
            break

    for i in range(0,len(porWave)):
        por = float(porWave[i])
        if por >=porThrld:
            porPos = i
            break

    if vccPos == -1 or porPos == -1:
        return False, 0
    else:
        print("vccPos=%d, vcc=%f, porPos=%d, por=%f" % (vccPos, vcc, porPos, por))
        return True, xincre*(porPos - vccPos)

def printWav(wav):

    s = ""
    for v in wav:
        f = 0
        try:
            f = float(v)
        except:
            pass
        if f < 0.5:
            s = s + "0 "
        else:
            s = s + "%1.2f " % f
    print("len=%d,WAV=%s" % (len(wav),s))

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00000010','00000000','00000100','00000010'])#VCC->src,osc1 POR->osc2
    ctx.sourcemeter.applyVoltage(3.3)
    ctx.tester.runCommand("test_mode_sel",0.2) # 获取SN
    # ctx.tester.runCommand("open_power_en",0.2)
    ctx.sourcemeter.applyVoltage(0)
    # ctx.oscilloscope.trigMul(2,'POS',0.7,scale = 0.05)
    ctx.oscilloscope.trig(2,'POS',1.3,scale = 0.5)
    # ctx.oscilloscope.trigMul(1,'POS',1.5,scale = 0.05)
    time.sleep(2)
    ctx.oscilloscope.statusCheck()
    time.sleep(2)
    ctx.sourcemeter.applyVoltage(3)
    for i in range(0,5):
        if ctx.oscilloscope.statusCheck() :
            break
        time.sleep(0.5)

    # input("m")
    if not ctx.oscilloscope.statusCheck() :
        return False
    vccWave = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
    porWave = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
    xincre = float(ctx.oscilloscope.xincre()) * 1000
    got, delay = calcDelay(xincre, vccWave, porWave, 2.9, 1.45)
    if got:
        ctx.logger.info("Tfpor = %f ms" % delay)
    else:
        ctx.logger.info("ERR: No Wave got or edge not found")
        printWav(vccWave)
        # print(porWave)
        return False

    ctx.sourcemeter.applyVoltage(0)
    time.sleep(1)
    # ctx.oscilloscope.trigMul(2,'POS',0.7,scale = 0.02)
    ctx.oscilloscope.trig(2,'POS',1.3,scale = 0.5)
    #ctx.oscilloscope.trigSlope(1,"PGReater",0.1,1.5,0.1)
    ctx.oscilloscope.statusCheck()
    time.sleep(2)
    ctx.sourcemeter.rampvol(0,3.0, 0.033,0.2)#(start,target,de,steps): 33ms->上升1v
    # time.sleep(1)
    for i in range(0,5):
        if ctx.oscilloscope.statusCheck() :
            break
        time.sleep(0.5)

    if not ctx.oscilloscope.statusCheck() :
        return False
    vccWave = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
    porWave = ctx.oscilloscope.readRamData(2,2,1,15625,'True')

    xincre = float(ctx.oscilloscope.xincre()) * 1000
    got, delay = calcDelay(xincre, vccWave, porWave, 1.5, 1.45)
    if got:
        ctx.logger.info("Tspor = %f ms" % delay)
    else:
        ctx.logger.info("ERR: No Wave got or edge not found")
        printWav(vccWave)
        return False

    return True
