# 求最大连续bit数
# 功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

# 输入：
# 一个byte型的数字
# 输出
# 对应的二进制数字中1的最大连续数
# 例：
# 输入 3
# 输出 2

import sys
try:
    while True:
        inputNum = int(sys.stdin.readline().split()[0])
        bitStr= bin(inputNum)
        maxContinueBitNum=0
        lastBitIndex=-1 #记录上一个bit位的位置
        for i in range(len(bitStr)):
            if bitStr[i]=='1':
                if lastBitIndex==-1:
                    lastBitIndex=i
                tempBitNum=i-lastBitIndex+1
                if(tempBitNum>maxContinueBitNum):
                    maxContinueBitNum=tempBitNum
            else:
                lastBitIndex=-1
        print(maxContinueBitNum)

except:
    pass