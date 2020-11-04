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
        if case =='S2.5':
            for i in range (0,len(data)-1,2):
                data [i] = str(int(data[i])-200)


    return SN, RESULT, data



def printCase(test_case, ts, sn, result, data):
    printCaseFuncName = ("print" + test_case).replace(".", "_")
    printCaseFunc = funcExist(printExt, printCaseFuncName)
    if printCaseFunc != False:
        printCaseFunc(test_case, ts, sn, result, data)
    # elif test_case in printExt.ptaFormatters:
    else:
        try:
            printExt.printWithFormatter(test_case, ts, sn, result, data)
        except:
            print("\t\tCASE %s for %s print Failed!" % (test_case, sn))


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
        print("Usage: %s logdir resultXLSX" % (sys.argv[0]))
        return

    dataDir = sys.argv[1]
    resultExcel = sys.argv[2]
    dataFiles = []

    for d in os.listdir(dataDir):
        dataFiles.append(dataDir + "/" + d)
    dataFiles.sort()

    for i in range(len(dataFiles)):
        parseFile(dataFiles[i])

    printExt.printAll(resultExcel)


if __name__ == "__main__":
    # 初始化终端ANSI颜色
    # colorama.init()
    try:
        main()
    except RuntimeError as e:
        print(e)
        sys.exit(-1)
