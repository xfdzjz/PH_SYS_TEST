
import time
title = "VDD稳定性测试"

desc = '''
    在时钟trim后做此项测试
    稳压源 Channel1 <=> VCC
    示波器 Channel3 <=> VDD
    示波器 Channel2 <=> POR
'''

def test(ctx):
    '''
    ctx为测试上下文对象，包含初始化好的各测试仪表
    ctx.sourcemeter 未使用
    ctx.multimeter 未使用
    '''
    # 芯片上电VCC=3V, Channel=1
    ctx.powersupply.voltageOutput(1, 3, 0.1, 3.3, 1)
    ctx.tester.runCommand("test_model_sel")
    ctx.tester.runCommand("open_power_en")

    # 设置Trigger检测VDD端口电压值是否低于1.35V， channel=3
    ctx.oscilloscope.trig(3,1.35,"NEGative")

    # HRC时钟选择8M,16M,1M分别执行FLASH 擦除，烧写，读取，IO作为输入\输出翻转等操作
    resp = ctx.tester.runCommand("test_vdd_stable")
    # ctx.sourcemeter.pulseTest(3,0,1)
    if resp != 'end':
        return False

    result = ctx.oscilloscope.statusCheck()
    print(result)
    if result == False:
        return result

    # 设置Trigger检测POR端口是否低电平， channel=2
    ctx.oscilloscope.trig(2,2,"NEGative")

    # HRC时钟选择8M,16M,1M分别执行FLASH 擦除，烧写，读取，IO作为输入\输出翻转等操作
    resp = ctx.tester.runCommand("test_vdd_stable")
    if resp != 'end':
        return False

    result = ctx.oscilloscope.statusCheck()
    return result

