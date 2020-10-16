
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

    # ctx.netmatrix.arrset(['00000000','00000000','00000000','00000000'])
    ctx.powersupply.voltageOutput(4, 0, 0.1, 3.3, 1)
    ctx.netmatrix.arrset(['00000000','00001000','00000000','00000000'])#ps4->gp15 1.21v

    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    resp= ctx.tester.runCommand("EnterEstMode",1)
    ctx.logger.info('1.1 '+resp)
    if resp != 'pass':
        return False

    resp=ctx.tester.runCommand("TestCmpTrim",1)
    ctx.logger.info('1.1 '+resp)
    # if resp == 'fail':
        #return False


    # Case S1.2
    ctx.powersupply.voltageOutput(4, 1.21, 0.1, 3.3, 1)
    time.sleep(0.5)
    resp = ctx.tester.runCommand("TestBGSTrim",1)
    ctx.logger.info('1.2 '+resp)
    # if resp == 'fail':
    #     return False


    # Case S1.3
    ctx.powersupply.voltageOutput(4, 1.22, 0.1, 3.3, 1)
    time.sleep(0.5)
    resp = ctx.tester.runCommand("TestBGATrim",1)
    ctx.logger.info('1.3 '+resp)

    # if resp == 'fail':
    #     return False
    ctx.powersupply.voltageOutput(4, 0, 0.1, 3.3, 1)


    # Case S1.4
    resp = ctx.tester.runCommand("TestHrcTrim",1)
    ctx.logger.info('1.4 '+resp)
    while resp != 'end':
        # if resp == 'fail':
        #     return False
        resp = ctx.tester.runCommand("next",1)
        ctx.logger.info('1.4 '+resp)

    # Case S1.5
    resp = ctx.tester.runCommand("TestLRCTrim",1)
    ctx.logger.info('1.5 '+resp)
    # if resp == 'fail':
    #     return False


    resp = ctx.tester.runCommand("TestMRCTrim",1)
    ctx.logger.info('1.6 '+resp)
    # if resp == 'fail':
    #     return False
    return True
