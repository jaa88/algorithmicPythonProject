
# 表示数字
# Catcher 是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入
# 一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况
# （abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
# （注意：记得加上while处理多个测试用例）

# 输入：
# 输入一个字符串
# 输出
# 返回有效密码串的最大长度
# 例：
# 输入 ABBA
# 输出 4

import sys

# 判断是否是密码
def judgeIsPassword(str):
    if(len(str)==1):
        return True
    else:
        for i in range(len(str)//2):
            if(str[i]!=str[-i-1]):
                return False
        return True




try:
    while True:
        inputStr = sys.stdin.readline().split()[0]
        maxNum=1
        for i in range(len(inputStr)-1):
            for j in range(i+1):
                if(judgeIsPassword(inputStr[j:j+len(inputStr)-i])):
                    if len(inputStr)-i >maxNum:
                        maxNum=len(inputStr)-i
        print(maxNum)

except:
    pass



























