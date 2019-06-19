

# 表示数字
# 判断短字符串中的所有字符是否在长字符串中全部出现

# 输入：
# 输入两个字符串。第一个为短字符，第二个为长字符。
# 输出
# true or false
# 例：
# 输入
#  bc
# abc
# 输出
# true

import sys

try:
    while True:
        inputStrA = sys.stdin.readline().split()[0]
        inputStrB = sys.stdin.readline().split()[0]

        setB=set()
        for i in inputStrB:
            setB.add(i)
        lenBBeforeAddA=len(setB)

        for i in inputStrA:
            setB.add(i)
        if(len(setB)!=lenBBeforeAddA):
            print("false")
        else:
            print("true")


except:
    pass



























