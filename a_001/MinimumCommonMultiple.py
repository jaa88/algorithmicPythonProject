# 求最小公倍数
# 正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

# 输入：
# 输入两个正整数A和B。
# 输出
# 输出A和B的最小公倍数。
# 例：
# 输入
# 5
# 7
# 输出
# 35
import sys


# 求最大公约数
def getMaxCommonDivisor(a, b):
    #保证a > b
    if (b > a):
        temp = a
        a = b
        b = temp

    c = a % b
    while (c != 0):
        a = b
        b = c
        c=a%b
    return b

#求最小公倍数
def getMinCommonMultiple(a,b):
    maxCommonDivisor=getMaxCommonDivisor(a,b)
    minCommonMultiple=a*b/maxCommonDivisor
    return minCommonMultiple

for line in sys.stdin:
    intputStrArr = line.split()
    numA = int(intputStrArr[0])
    numB = int(intputStrArr[1])
    maxCommonMultiple = getMinCommonMultiple(numA, numB)
    print(int(maxCommonMultiple))



