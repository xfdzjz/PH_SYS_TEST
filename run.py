# -*- coding: utf-8 -*-
import sys, os
import argparse
import chardet
import importlib, colorama

import config
from lib.SourceMeter import SourceMeter
from lib.PowerSupply import PowerSupply
from lib.MultiMeter import MultiMeter
from lib.Oscilloscope import Oscilloscope
from lib.Tester import Tester
from lib.NetMatrix import NetMatrix


def initDevices(config):
    '''
    初始化外部设备、仪表
    '''
    class TestContext:
        pass

    context = TestContext()
    context.sourcemeter = SourceMeter(config.sourcemeter)
    context.powersupply = PowerSupply(config.powersupply)
    context.multimeter = MultiMeter(config.multimeter)
    context.oscilloscope = Oscilloscope(config.oscilloscope)
    context.tester = Tester(config.tester)
    context.netmatrix = NetMatrix(config.netmatrix)
    # 停止仪表待重新接线
    context.sourcemeter.stopAll()
    context.powersupply.stopAll()
    context.multimeter.stopAll()
    context.oscilloscope.stopAll()
    context.tester.stopAll()
    context.netmatrix.stopAll()
    return context

def execute_case(case, caseDir, context):
    '''
    加载对应模块，执行测试用例
    '''
    # 加载用例模块
    spec = importlib.util.spec_from_file_location("test", caseDir + '/case.py')
    caseModule = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = caseModule
    spec.loader.exec_module(caseModule)

    # 执行测试用例
    print("=====  TEST CASE %s [ %-35s ] =====" % (case, caseModule.title))
    print(caseModule.desc)
    input("Press ENTER to begin")
    result = caseModule.test(context)
    print("TEST CASE %-50s ...... [ %s ]" % (case,
        "\033[1;32mPASS\033[0m" if result else "\033[1;31mFAILED\033[0m"))

    # 停止仪表待重新接线
    context.sourcemeter.stopAll()
    context.powersupply.stopAll()
    context.multimeter.stopAll()
    context.oscilloscope.stopAll()
    context.tester.stopAll()
    context.netmatrix.stopAll()
    print()


def main():
    '''
    主程序
    '''
    # 初始化外设
    context = initDevices(config)

    # 获得用例列表
    mainDir = os.path.split(os.path.realpath(__file__))[0]
    availableCases = []
    for d in os.listdir(mainDir + "/cases/"):
        availableCases.append(d)
    availableCases.sort()

    # 获得命令行参数
    parser = argparse.ArgumentParser(description='Phoenix CP test tool')
    parser.add_argument('cases', help="Test cases", nargs='*', choices=availableCases)
    args = parser.parse_args()
    cases = args.cases

    # 执行命令行的全部用例
    while len(cases) > 0:
        caseDir = mainDir + "/cases/" + cases[0]
        execute_case(cases[0], caseDir, context)
        cases.pop(0)


if __name__ == "__main__":
    # 初始化终端ANSI颜色
    colorama.init()
    try:
        main()
    except RuntimeError as e:
        print(e)
        sys.exit(2)
