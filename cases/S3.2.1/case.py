
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
    time.sleep(0.250)
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    ctx.oscilloscope.trigMul(2,'POS',0.7, scale = 0.01)
    ctx.oscilloscope.trigSlope(1,"PGReater",0.2,1.5)
    ctx.sourcemeter.rampvol(0,3.3,0.2,0.1)

=======
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    ctx.oscilloscope.trigMul(2,'POS',0.7, scale = 0.01)
    ctx.oscilloscope.trigSlope(1,"PGReater",0.2,1.5)
    time.sleep(3)
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    vol1 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
    vol = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
    if ctx.oscilloscope.statusCheck() == False:
        return False
<<<<<<< HEAD
    print(vol)
    print(vol1)
    input('n')
    time.sleep(1)
    ctx.oscilloscope.trigMul(2,'NEG',0.7,scale = 0.1)
    ctx.oscilloscope.trigSlope(1,"PNGReater",0.2,1.5)

    ctx.sourcemeter.rampvol(3.3,0,0.2,0.1)
    vol2 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')# readRamData(self,channel,count,start,final, do ='false'):
    vol3 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')

    print(vol)


    for i in range(0,len(vol)):
        if float(vol[i]) >= 1.45:
            ctx.logger.info ('osc1 data is %f when osc2 greater than 1.5' %float(vol1[i]))
            ctx.logger.debug ('osc1 data is %f when osc2 greater than 1.5' %float(vol1[i]))
            break
        else:
            ctx.logger.info('there is no osc1 data')


    for i in range(0,len(vol2)):
        if float(vol2[i]) <= 1.3:
            ctx.logger.info ('osc1 data is %f when osc2 less than 1.5' %float(vol3[i]))
            break
        else:
            ctx.logger.info('there is no osc2 data')
=======
    time.sleep(1)
    ctx.oscilloscope.trigMul(2,'NEG',0.7,scale = 0.1)
    ctx.oscilloscope.trigSlope(1,"PNGReater",0.2,1.5)
    time.sleep(3)
    ctx.sourcemeter.rampvol(3.3,0,0.1,0.2)
    vol2 = ctx.oscilloscope.readRamData(2,2,1,15625,'True')
    ctx.logger.info(vol2)
    vol3 = ctx.oscilloscope.readRamData(1,2,1,15625,'True')
    ctx.logger.info(vol3)
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

    for i in range(0,len(vol)):
        if float(vol[i]) >= 1.5:
            ctx.logger.info (float(vol1[i]))
            ctx.logger.debug (float(vol1[i]))
            ctx.logger.info (float(vol1[i]))
            ctx.logger.debug(float(vol1[i])

    for i in range(0,len(vol2)):
        if float(vol2[i]) <= 1.5:
            ctx.logger.info (float(vol3[i]))
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6



    if ctx.oscilloscope.statusCheck() == False:
        return False
    return True
