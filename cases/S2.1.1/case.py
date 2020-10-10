
import time
import pandas as pd
from pandas import Series
import openpyxl
import re
title = "VBGS随VCC变化"

desc = '''
relay k25 connect

'''

def test(ctx):
    '''
    '''
    # 芯片上电VCC=3V, Channel=1

    ctx.netmatrix.arrset(['00000010','00000000','00000000','00000000'])#VBG->sourmeter
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 3.3, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("VBGSTestOnVCCVerify",1)

    vol = []
    vcc = [3.3,5,2.2]

    while resp !='end':
        ctx.logger.info(resp)
        input('n')
        if resp == 'ready':
            vol.append(ctx.sourcemeter.volTest())
            ctx.logger.info("VCC is 3.3v vol is %f" %vol[0])
            ctx.powersupply.voltageOutput(3, 5, 0.1, 6, 1)
            vol.append(ctx.sourcemeter.volTest())
            ctx.logger.info("VCC is 5.0v vol is %f" %vol[1])
            ctx.powersupply.voltageOutput(3, 2.2, 0.1, 5, 1)
            vol.append(ctx.sourcemeter.volTest())
            ctx.logger.info("VCC is 2.2v vol is %f" %vol[2])

        else:
            return False
        resp = ctx.tester.runCommand("next")





    return True
