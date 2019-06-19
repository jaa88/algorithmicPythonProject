
# 表示数字
# 将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变

# 输入：
# 输入一个字符串
# 输出
# 字符中所有出现的数字前后加上符号“*”，其他字符保持不变
# 例：
# 输入 Jkdi234klowe90a3
# 输出 Jkdi*234*klowe*90*a*3*

import sys

def judgeCharIsNum(c):
    if(ord(c)>=ord("0") and ord(c)<=ord("9")):
        return True
    else:
        return False

try:
    while True:
        inputStr = sys.stdin.readline().split()[0]
        # 定义一个数组，不断往里面拼字符、字符串
        returnArr=[]
        lastCharIsNumFlag=False
        for i in range(len(inputStr)):
            targetChar=inputStr[i]
            if(judgeCharIsNum(targetChar)):
                #  若前一个字符不是数字
                if(not lastCharIsNumFlag):
                    returnArr.append("*"+targetChar)
                else:
                    returnArr.append(targetChar)
                # 最后一个是数字的话，后面要单独拼接*
                if(i==len(inputStr)-1):
                    returnArr.append("*")
                lastCharIsNumFlag = True
            else:
                #  若前一个字符不是数字
                if (not lastCharIsNumFlag):
                    returnArr.append(targetChar)
                else:
                    returnArr.append("*"+targetChar)
                lastCharIsNumFlag=False
        print("".join(returnArr))
except:
    pass



























