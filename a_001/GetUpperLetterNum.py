
# 找出给定字符串中大写字符(即'A'-'Z')的个数
# 接口说明
# 原型：int CalcCapital(String str);
# 返回值：int

# 输入：
# 输入一个字符串
# 输出
# 输出string中大写字母的个数
# 例：
# 输入 add123#$%#%#O
# 输出 1

import sys

try:
    while True:
        inputStr = sys.stdin.readline().split()[0]
        upperCharNum=0
        for i in inputStr:
            if(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                upperCharNum=upperCharNum+1
        print(upperCharNum)

except:
    pass