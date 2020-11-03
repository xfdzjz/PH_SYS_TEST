import re
import time

# 可以用正则表达式来解析输出结果的用例
ptaParsers = {
    'S2.1.1': 'vol is (\S+)',
    'S2.1.2': 'vol is (\S+)',
    'S2.1.3': 'fre is (\S+), duty is (\S+)',
    'S2.1.4': 'fre is (\S+), duty is (\S+)',
    'S2.1.5': 'fre is (\S+), duty is (\S+)',
    'S2.1.6': 'avg is (\S+)',
    'S2.2.1': 'vol is (\S+)',
    'S2.2.3': 'vol is (\S+)',
    'S2.2.4': 'vol is (\S+)',
    'S2.2.6': 'vol is (\S+)',
    'S2.2.7': 'VCC is \S+v vol is (\S+)',
    'S2.2.8': 'ready:(\S+)mv VCC is (\S+)v avg is (\S+)',
    'S2.2.9': 'ready:(\S+)mv VCC is (\S+)v avg is (\S+)',
    'S2.2.10': 'vol is (\S+)',
    'S2.2.11': 'vol is (\S+)',
    'S2.3': 'ISRCS amp is (\S+) uA when VCC is \S+v',
    'S2.4.1': 'INFO: result\d+mv:(\d+)',
    'S2.4.2': 'NOTHING',  # nothinf to parse
    # 'S2.5': '(Right now|final result) is (\d+)mv',
    'S2.5': ' is (\d+)mv',
    'S2.6.1': 'indled amp is (\S+) when VCC is (\S+)v',
    'S2.7.1': 'ready:(\S+)mv VCC is (\S+)v avg is (\S+)',  # not tested yet
    'S2.7.2': 'ready:(\S+)mv VCC is (\S+)v avg is (\S+)',  # not tested yet
    'S2.8.1': 'resp is\s+(\S+).*?apply (\S+)',  # not tested yet
    'S2.8.2': 'ready:(\S+)mv VCC is (\S+)v avg is (\S+)',  # not tested yet
    'S2.8.3': 'ready:(\S+)mv VCC is (\S+)v avg is (\S+)',  # not tested yet
    'S2.8.4': 'ready:(\S+)mv VCC is (\S+)v avg is (\S+)',  # not tested yet

    'S3.1.1': 'amp is (\S+) mA when VCC is \S+v',
    'S3.1.2': 'amp is (\S+) mA when VCC is \S+v',
    'S3.1.3': 'amp is (\S+) mA when VCC is \S+v',
    'S3.1.4': 'amp is (\S+) mA when VCC is \S+v',
    'S3.1.5': 'amp is (\S+) mA when VCC is \S+v',
    'S3.5': 'VCC (\S+) V ',
    'S3.2.2': '= (\S+) ms',
    'S3.3.1': 'amp is (\S+) mA when VCC is (\S+)v',
    'S3.3.2': 'amp is (\S+) mA when sourmeter is (\S+)v',
    'S3.3.3': 'amp is (\S+) mA when VCC is (\S+)v',
    'S3.4': 'duty is (\S+), fre is (\S+)',

    'S4.1': 'NOTHING',  # nothinf to parse
    "S4.2": 'AIN=(\S+),vol=(\S+), RESP=(\S+)',

    "S5": 'AIN=(\S+),vol=(\S+), RESP=(\S+)',

    "S6.1": 'duty is (\S+) percent, frequency is (\S+)',
    "S6.2": 'vok\d vol is (\d+)mv',
    "S6.3": 'LX neg val is (\S+) when VH is (\S+)',
}

# 特殊的解析函数，函数名为parseCase_Name
# CaseName经过.=>_变换


# def parseS2_1_11(case, lines):
#     return re.findall(ptaParsers[case], lines, re.DOTALL | re.MULTILINE)


if __name__ == "__main__":
    print(ptaParsers)
