
import time

# 可以用格式化字符串输出结果的用例
ptaFormatters = {
    'S3.2.1': [[0, 3], "VTR=%s\nVTF=%s"],
    'S3.2.2': [[0, 1], "Tfpor=%s\nTspor=%s"],
}

# 特殊的输出函数，函数名为printCase_Name
# CaseName经过.=>_变换


def printS2_1_1(test_case, ts, sn, result, data):
    exectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    print("用例:%s, 执行时间:%s, SN=%s, 执行结果: %s" %
          (test_case, exectime, sn, result))
    print(data)


if __name__ == "__main__":
    print(ptaFormatters)
