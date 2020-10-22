import sys
import os
import re
import time

import parseExt
import printExt
# from parseExt import ptaParsers
# from printExt import ptaFormatters


def funcExist(module, funcName):
    try:
        func = getattr(module, funcName)
        if callable(func):
            return func
        else:
            return False
    except:
        return False


def parseCase(case, lines):
    '''
    解析输出内容(数组)
    '''
    SN = "UNKNOWN"
    RESULT = "UNKNOWN"
    data = []
    matchObj = re.search('\.\.\.\.\.\. SN=(\d+).*?(PASS|FAIL)', lines)
    if (matchObj):
        SN = matchObj.group(1)
        RESULT = matchObj.group(2)

    parseCaseFuncName = ("print" + case).replace(".", "_")
    parseCaseFunc = funcExist(parseExt, parseCaseFuncName)
    if parseCaseFunc != False:
        data = parseCaseFunc(case, lines)
    elif case in parseExt.ptaParsers:
        data = re.findall(
            parseExt.ptaParsers[case], lines, re.DOTALL | re.MULTILINE)
    return SN, RESULT, data


def printWithFormatter(test_case, ts, sn, result, data):
    exectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    print("用例:%s, 执行时间:%s, SN=%s, 执行结果: %s" %
          (test_case, exectime, sn, result))
    params = []  # 输出参数， 数组
    allParams = []
    fmtFilter = printExt.ptaFormatters[test_case][0]  # 参数过滤器
    fmt = printExt.ptaFormatters[test_case][1]  # 打印格式
    for t in data:  # data为元组数组, 展开成一维数组allParams
        if isinstance(t,tuple):
            t = list(t)
            allParams.extend(t)
        elif isinstance(t,list):
            allParams.extend(t)
        else:
            allParams.append(t)
    for i in fmtFilter:
        params.append(allParams[i])
    params = tuple(params)  # 转元组供打印
    print(fmt % params)
    print()


def printDefault(test_case, ts, sn, result, data):
    exectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    print("用例:%s, 执行时间:%s, SN=%s, 执行结果: %s" %
          (test_case, exectime, sn, result))
    print(data)
    print()


def printCase(test_case, ts, sn, result, data):
    printCaseFuncName = ("print" + test_case).replace(".", "_")
    printCaseFunc = funcExist(printExt, printCaseFuncName)
    if printCaseFunc != False:
        printCaseFunc(test_case, ts, sn, result, data)
    elif test_case in printExt.ptaFormatters:
        printWithFormatter(test_case, ts, sn, result, data)
    else:
        printDefault(test_case, ts, sn, result, data)


def parseFile(filename):
    '''
    解析一个log文件
    '''
    with open(filename, 'r', encoding='gb2312') as reader:
        output = ''
        test_case = ''
        ts = 0
        for line in reader:
            # 找到CASE第一行，解析(时间，CASE, SN)
            matchObj = re.match(
                '(\d+-\d+-\d+ \d+:\d+:\d+).* =====  TEST CASE (\S+) .*', line)
            if matchObj:
                if test_case != '':  # 本行之前的内容提交
                    sn, result, data = parseCase(test_case, output)
                    printCase(test_case, ts, sn, result, data)
                # 本行以下的内容属于一个新CASE输出
                ts = time.strptime(matchObj.group(1), "%Y-%m-%d %H:%M:%S")
                ts = int(time.mktime(ts))
                test_case = matchObj.group(2)
                output = ''
            else:
                output += line
        # 文件最后的内容提交
        if test_case != '' and output != '':
            sn, result, data = parseCase(test_case, output)
            printCase(test_case, ts, sn, result, data)


def main():
    if len(sys.argv) == 1:
        print("Usage: %s logfile1 [logfile2] ..." % (sys.argv[0]))
        return

    # 如果模块中有需要初始化的部分，比如打开数据库可以在init函数实现
    # initFunc = funcExist(parseExt, "init")
    # if initFunc != False:
    #     initFunc()
    # initFunc = funcExist(printExt, "init")
    # if initFunc != False:
    #     initFunc()

    for i in range(1, len(sys.argv)):
        parseFile(sys.argv[i])


if __name__ == "__main__":
    # 初始化终端ANSI颜色
    # colorama.init()
    try:
        main()
    except RuntimeError as e:
        print(e)
        sys.exit(2)
