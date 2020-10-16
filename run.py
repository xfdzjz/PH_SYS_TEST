# -*- coding: utf-8 -*-
import sys, os, time
import argparse
import chardet
import importlib, colorama
import logging  # 引入logging模块
import re
import config
from lib.SourceMeter import SourceMeter
from lib.PowerSupply import PowerSupply
from lib.Oscilloscope import Oscilloscope
from lib.Tester import Tester
from lib.NetMatrix import NetMatrix

def initLogger(fileName):
    logger = logging.getLogger('CASE')
    logger.setLevel(logging.DEBUG)  # Log等级总开关
    logger.addHandler(logging.StreamHandler())
    if fileName :
        fileHandler = logging.FileHandler(fileName)
        fileHandler.setLevel(logging.INFO)  # 输出到file的log等级的开关
        fileHandler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s"))
        logger.addHandler(fileHandler)
    return logger

def initLogger(fileName):
    logger = logging.getLogger('CASE')
    logger.setLevel(logging.DEBUG)  # Log等级总开关
    logger.addHandler(logging.StreamHandler())
    if fileName :
        fileHandler = logging.FileHandler(fileName)
        fileHandler.setLevel(logging.INFO)  # 输出到file的log等级的开关
        fileHandler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s"))
        logger.addHandler(fileHandler)
    return logger

def initDevices(config):
    '''
    初始化外部设备、仪表
    '''
    class TestContext:
        pass

    context = TestContext()
    try:
        context.sourcemeter = SourceMeter(config.sourcemeter)
        context.powersupply = PowerSupply(config.powersupply)
        context.oscilloscope = Oscilloscope(config.oscilloscope)
        context.tester = Tester(config.tester)
        context.netmatrix = NetMatrix(config.netmatrix)
    except Exception as e:
        print("仪表初始化错误，请检查连接")
        print(e)
        return None

    # 停止仪表待重新接线
    context.sourcemeter.stopAll()
    context.powersupply.stopAll()
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
    context.logger.info("=====  TEST CASE %s [ %-35s ] =====" % (case, caseModule.title))
    context.logger.debug(caseModule.desc)
    result = caseModule.test(context)
    context.logger.info("TEST CASE %-50s ...... SN=%s [ %s ]" % (case, context.tester.SN,
        "\033[1;32mPASS\033[0m" if result else "\033[1;31mFAILED\033[0m"))

    # 停止仪表待重新接线
    context.sourcemeter.stopAll()
    context.powersupply.stopAll()
    context.oscilloscope.stopAll()
    context.tester.stopAll()
    context.netmatrix.stopAll()
    context.logger.debug("")


def main():
    '''
    主程序
    '''
    # 初始化外设
    context = initDevices(config)
    if context == None:
        return

    # 获得命令行参数
    parser = argparse.ArgumentParser(description='Phoenix CP test tool')
    parser.add_argument('casefilter', help="Test cases")
    parser.add_argument("-o", "--output", default=None)
    args = parser.parse_args()
    if args.output:
        context.logger = initLogger(args.output)
    else:
        context.logger = initLogger(None)

    # 获得用例列表
    mainDir = os.path.split(os.path.realpath(__file__))[0]
    cases = []
    # 将命令行参数casefilter作为正则表达式过滤cases
    casefilter =  "^" + args.casefilter + "$"
    casefilter = casefilter.replace(".","\\.")
    casefilter = casefilter.replace("*",".*")
    for d in os.listdir(mainDir + "/cases/"):
        if re.match(casefilter, d):
            cases.append(d)
    cases.sort()

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
