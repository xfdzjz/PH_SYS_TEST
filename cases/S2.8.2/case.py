import time
import re
title = "ADC参考电压遍历"

desc = '''
    relay k5,k14 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''
    count = 0
    step = 0
    ad_vol = []
    counter = []
    b=0
    a=0
    vol1 =['0']
    vrvol =[]
    vref = []
    data = []
    inlM = 0
    dnlM = 0
    step = 0
    lsb = 0
    inl = []
    inl1 = 0
    dnl = []
    dnl1 = 0
    ad_vol = []
    counter = []
    # 芯片上电VCC=3V
    ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])#GP04->src GP14->vref
    ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
<<<<<<< HEAD

    time.sleep(0.250)
    b=b+1
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_adc_int_vref")
    count = 0
    k=0
    with open('temp.txt') as f:
        for i in range(0,3):
            data.append(f.readline())
        for i in range(3,12):
            data.append(f.readline())
            search = re.match( r'(.*?) VCC is (.*) avg is (.*)', data[i], re.M|re.I|re.S)
            if search:
                chip=search.groups(0)
                vref.append(float(chip[0]))
                vrvol.append(float(chip[2]))
=======
    time.sleep(0.250)
    #ctx.tester.runCommand("test_mode_sel")
    ctx.tester.runCommand("open_power_en")
    resp = ctx.tester.runCommand("test_adc_int_vref")
    count = 0
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6

    while resp !="end":
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp =='ready':
            resp = ctx.tester.runCommand("next")
        if resp[-2:] == 'mv':
            vol = float(resp[:-2])
<<<<<<< HEAD
            step = (vol-100) / 4096



        for count in range(0,6):
            ctx.sourcemeter.applyVoltage(count*step+0.5*step)
            lsb = vrvol[b-1]/4095
            resp = ctx.tester.runCommand("n")
            inl1 = (int(resp[0:3],16)*lsb - count*step-0.5*step)/lsb
            dnl1 = float(int(resp[0:3],16)) - float(int(vol1[a],16))
            a=a+1
            print(a)
            print(count)
            vol1.append(resp[0:3])
            inl.append(inl1)
            dnl.append(dnl1)
            #ad_vol.append(inl1/dnl1)
            ctx.logger.info("inl is %f" %float(inl1))
            ctx.logger.info("dnl is %f" %float(dnl1))
            ctx.logger.info("resp is %s" %resp)
            ctx.logger.info('vol apply %f' %(count*step+0.5*step))
        inlM = max(inl[2*k*6:(2*k+1)*6])
        dnlM = max(dnl[2*k*6:(2*k+1)*6])
        print("inlM is %f" %inlM)
        print("dnlM is %f" %dnlM)


        for count in range(6,0,-1):#
            print(count)
            print(a)
            ctx.sourcemeter.applyVoltage(count*step+0.5*step)
            lsb = vrvol[b-1]/4095
            resp = ctx.tester.runCommand("n")
            inl1 = (int(resp[0:3],16)*lsb - count*step-0.5*step)/lsb
            dnl1 = float(int(resp[0:3],16)) - float(int(vol1[a-1],16))+1
            a=a+1
            vol1.append(resp[0:3])
            inl.append(inl1)
            dnl.append(dnl1)
            ad_vol.append(inl1/dnl1)

            ctx.logger.info("inl is %f" %float(inl1))
            ctx.logger.info("dnl is %f" %float(dnl1))
            ctx.logger.info("resp is %s" %resp)
            ctx.logger.info('vol apply %f' %(count*step+0.5*step))
        inlM = max(inl[(2*k+1)*6:(2*k+2)*6])
        dnlM = max(dnl[(2*k+1)*6:(2*k+2)*6])
        print("inlM is %f" %inlM)
        print("dnlM is %f" %dnlM)

        resp = ctx.tester.runCommand("n")

        b=b+1


=======
            step = vol / 4096
        for count in (0,4096):
            ctx.sourcemeter.applyVoltage(count*step)
            resp = ctx.tester.runCommand("n")
            ctx.logger.info(resp)
            ad_vol.append(resp)
            counter.append(count)
        for count in (4096,0):
            ctx.sourcemeter.applyVoltage(count*step)
            count = count -1
            resp = ctx.tester.runCommand("n")
            ctx.logger.info(resp)
            ad_vol.append(resp)
            counter.append(count)
        resp = ctx.tester.runCommand("n")

    for (x,y) in (ad_vol,counter):
        ctx.logger.info("case %d voltage is %f"%(y,x))
>>>>>>> 7146e1e0af3dc1479c688f0e0bdd636a80c8a0c6


    print('pass')
    return True
