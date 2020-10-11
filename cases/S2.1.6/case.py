
import time
title = "Voltref模块"

desc = '''
 relay k15 connect
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.netmatrix.arrset(['00010000','00000000','00000000','00000000'])#GP14->OSC
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(0.250)
<<<<<<< HEAD
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
=======
    ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6
    resp = ctx.tester.runCommand("test_volt_ref")
    a =[2500,2000,1500,1200]
    i = 0
    with open('temp.txt','w') as f:
        while resp !='end':
            ctx.logger.info(resp)
            ctx.logger.debug(resp)
            if resp[0:5] == 'ready':
                avg = ctx.sourcemeter.volTest()
                ctx.logger.info("VCC is 3.3v avg is %s" %(avg))
                ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
                avg1 = ctx.sourcemeter.volTest()
                ctx.logger.info("VCC is 5v avg is %s" %(avg1))
                ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
                avg2 = ctx.sourcemeter.volTest()
                ctx.logger.info("VCC is 2.2v avg is %s" %(avg2))
                ctx.powersupply.voltageOutput(3, 3.3, 0.1, 6, 1)

<<<<<<< HEAD
                f.write("%d VCC is 3.3v avg is %s\n" %(a[i],avg))
                f.write("%d VCC is 5v avg is %s\n" %(a[i],avg1))
                f.write("%d VCC is 2.2v avg is %s\n" %(a[i],avg2))
                i=i+1
            else:
                return False
            resp = ctx.tester.runCommand("next")
    f.close()
=======
    while resp !='end':
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp[0:5] == 'ready':
            ctx.sourcemeter.applyVoltage(2)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            ctx.logger.info("VCC is 3.3v avg is %s" %(avg))
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            ctx.logger.info("VCC is 5v avg is %s" %(avg))
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            para = ctx.oscilloscope.volTest(2)
            avg = para[1]
            ctx.logger.info("VCC is 2.2v avg is %s" %(avg))
            ctx.powersupply.voltageOutput(3, 3.3, 0.1, 6, 1)
        else:
            return False
        resp = ctx.tester.runCommand("next")
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6

    return True
