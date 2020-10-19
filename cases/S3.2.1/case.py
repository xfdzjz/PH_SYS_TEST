
import time
title = "POR功能"

desc = '''
     relay k25,K23 connect
'''
filename = '3.2.1data.txt'
def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00000010','00000000','00000100','00000010'])#VCC->src，osc1 por->osc2
    ctx.sourcemeter.applyVoltage(3.3)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)

    ctx.oscilloscope.trigMul(2,'POS',0.7, scale = 0.5)
    #ctx.oscilloscope.trigSlope(1,"PGReater",0.2,1.5,0.6)
    ctx.sourcemeter.rampvol(0,3.3,0.2,0.1)

    vol1 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
    vol = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
    if ctx.oscilloscope.statusCheck() == False:
        return False
    # print(vol)
    # print(vol1)

    time.sleep(1)

    ctx.oscilloscope.trigMul(2,'NEG',0.7,scale = 0.5)
    #ctx.oscilloscope.trigSlope(1,"PNGReater",0.2,1.5)
    ctx.sourcemeter.rampvol(3.3,0,0.2,-0.1)#rampvol(self,start,target,de,steps):
    vol2 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')# readRamData(self,channel,count,start,final, do ='false'):
    vol3 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')

    # print(vol2)
    # print(vol3)

    for i in range(0,len(vol)):
        if float(vol[i]) >= 1.45 :
            ctx.logger.info ('osc1 data is %f when osc2 greater than 1.5' %float(vol1[i]))
            break
        elif i == len(vol) -1 :
            ctx.logger.info('there is no osc1 data')
            return False


    for i in range(0,len(vol3)):
        if float(vol3[i]) <= 1.3:
            ctx.logger.info ('osc1 data is %f when osc2 less than 1.5' %float(vol2[i]))
            break
        elif i == len(vol) -1 :
            ctx.logger.info('there is no osc2 data')
            return False



    if ctx.oscilloscope.statusCheck() == False:
        return False
    return True
