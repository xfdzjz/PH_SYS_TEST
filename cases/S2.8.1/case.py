import time
import re
title = "ADC采样速率遍历4MHz~500KHz"

desc = '''
    relay k5,k14 connect
'''



def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.multimeter 未使用
    ctx.oscilloscope  未使用
    '''
    vref =[]
    vrvol =[]
    count = 0
    data =[]
    inlM = 0
    dnlM = 0
    inlN = []
    dnlN = []
    step = 0
    lsb = 0
    inl = []
    inl1 = 0
    dnl = []
    dnl1 = 0
    ad_vol = []
    counter = []
    vol1 = ['0']
    a = 0
    b=0
    with open('temp.txt','r') as f:
        for i in range(0,3):
            data.append(f.readline())
            search = re.match( r'(.*?) VCC is (.*) avg is (.*)', data[i], re.M|re.I|re.S)
            if search:
                chip=search.groups(0)
                vref.append(float(chip[0]))
                vrvol.append(float(chip[2]))

    # 芯片上电VCC=3V
    #ctx.powersupply.voltageOutput(3, 3.3, 0.1, 5, 1)
    #ctx.netmatrix.arrset(['01000000','00010000','00000000','00000000'])#GP04->src GP14->vref
    ctx.powersupply.voltageOutput(3, 2.3, 0.1, 5.6, 1)
    time.sleep(0.250)
    ctx.tester.runCommand("test_mode_sel",0.2)
    ctx.tester.runCommand("open_power_en",0.2)
    resp = ctx.tester.runCommand("test_adc_freq")
    count = 0
    k=0
    b=b+1

    while resp !="end":
        ctx.logger.info(resp)
        ctx.logger.debug(resp)
        if resp =='ready':
            resp = ctx.tester.runCommand("next")
        if resp[-2:] == 'mv':
            vol = float(resp[:-2])
            step = (vol-100) / 4095 /1000
        #ctx.sourcemeter.applyVoltage(((1.34-23*0.000654)*1.5))
        for count in range(-1,4096):#-1->4096
            ctx.sourcemeter.applyVoltage(count*step+0.5*step)

            #time.sleep(0.1)
            lsb = vrvol[b-1]/4095
            resp = ctx.tester.runCommand("n")
            print(resp)
            inl1 = (int(resp[0:3],16)*lsb - count*step-0.5*step)/lsb
            dnl1 = float(int(resp[0:3],16)) - float(int(vol1[a],16))
            a=a+1
            vol1.append(resp[0:3])
            #ad_vol.append(inl1/dnl1)
            ctx.logger.info("inl is %f" %float(inl1))
            ctx.logger.info("dnl is %f" %float(dnl1))
            ctx.logger.info("resp is %s" %resp)
            ctx.logger.info('vol apply %f' %(count*step+0.5*step))
            ctx.logger.info("vref is %f" %float(vrvol[b-1]))
            # if count %1000 ==0:
            #     ctx.sourcemeter.volt.disconnect()
            #     time.sleep(1)
            #     ctx.sourcemeter.volt.connect()
            #     time.sleep(2)


        #inlM = max(inl[2*k*6:(2*k+1)*6])
        #dnlM = max(dnl[2*k*6:(2*k+1)*6])




        for count in range(4095,-2,-1):#4095,-2,-1
            print(count)
            ctx.sourcemeter.applyVoltage(count*step+0.5*step)
            lsb = vrvol[b-1]/4095
            resp = ctx.tester.runCommand("n")
            inl1 = (int(resp[0:3],16)*lsb - count*step-0.5*step)/lsb
            dnl1 = float(int(resp[0:3],16)) - float(int(vol1[a-1],16))+1
            a=a+1
            vol1.append(resp[0:3])
            #ad_vol.append(inl1/dnl1)

            ctx.logger.info("inl is %f" %float(inl1))
            ctx.logger.info("dnl is %f" %float(dnl1))
            ctx.logger.info("resp is %s" %resp)
            ctx.logger.info('vol apply %f' %(count*step+0.5*step))
            ctx.logger.info("vref is %f" %float(vrvol[b-1]))

            # if count %1000 ==0:
            #     ctx.sourcemeter.volt.disconnect()
            #     time.sleep(1)
            #     ctx.sourcemeter.volt.connect()
            #     time.sleep(2)



        # inlM = max(inl[(2*k+1)*6:(2*k+2)*6])
        # dnlM = max(dnl[(2*k+1)*6:(2*k+2)*6])
        # print("inlM is %f" %inlM)
        # print("dnlM is %f" %dnlM)
        input('n')

        resp = ctx.tester.runCommand("n")
        k = k+1
        if k == 6 :
            ctx.powersupply.voltageOutput(3, 5.0, 0.1, 6, 1)
            b=b+1


        if k == 7 :
            ctx.powersupply.voltageOutput(3, 2.3, 0.1, 5, 1)
            b=b+1

        if a == 83: #a=4097*2*7
            resp = ctx.tester.runCommand("n")

    print('pass')
    return True
