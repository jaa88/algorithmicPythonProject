
# 表示数字
# 密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。
#        一、密码长度:
#        5 分: 小于等于4 个字符
#        10 分: 5 到7 字符
#        25 分: 大于等于8 个字符
#        二、字母:
#        0 分: 没有字母
#        10 分: 全都是小（大）写字母
#        20 分: 大小写混合字母
#        三、数字:
#        0 分: 没有数字
#        10 分: 1 个数字
#        20 分: 大于1 个数字
#        四、符号:
#        0 分: 没有符号
#        10 分: 1 个符号
#        25 分: 大于1 个符号
#        五、奖励:
#        2 分: 字母和数字
#        3 分: 字母、数字和符号
#        5 分: 大小写字母、数字和符号
#        最后的评分标准:
#        >= 90: 非常安全
#        >= 80: 安全（Secure）
#        >= 70: 非常强
#        >= 60: 强（Strong）
#        >= 50: 一般（Average）
#        >= 25: 弱（Weak）
#        >= 0:  非常弱
#
# 对应输出为：
#   VERY_WEAK,
#    WEAK,
#    AVERAGE,
#    STRONG,
#    VERY_STRONG,
#    SECURE,
#    VERY_SECURE

# 输入：
# 输入一个string的密码
# 输出
# 输出密码等级
# 例：
# 输入 38$@NoNoNo
# 输出 VERY_SECURE

import sys


# 密码长度得分
def getPasswordLengthScore(str):
    strLength = len(str)
    if (strLength <= 4):
        return 5
    if (strLength <= 7):
        return 10
    else:
        return 25


# 密码的字母得分
def getPasswordLetterScore(lowerLetterNum, upperLetterNum):
    if lowerLetterNum == lowerLetterNum and lowerLetterNum == 0:
        return 0
    if lowerLetterNum > 0 and upperLetterNum > 0:
        return 20
    return 10


# 密码的数字得分
def getPasswordNumberScore(num):
    if (num == 0):
        return 0
    if num == 1:
        return 10
    return 20


# 密码的其他符号得分
def getPasswordOtherCharNumScore(num):
    if (num == 0):
        return 0
    if num == 1:
        return 10
    return 25


def getExtraRewardScore(lowerLetterNum, upperLetterNum, numberNum, otherCharNum):
    if numberNum > 0 and (lowerLetterNum > 0 or upperLetterNum > 0):
        if lowerLetterNum > 0 and upperLetterNum > 0 and otherCharNum > 0:  # 大小字母、字符也有
            return 5
        if otherCharNum > 0:  # 大小字母存在歧义、字符也有
            return 3
        return 2
    else:
        return 0


# 根据分数得出等级
def getTargetLevelByScore(score):
    if (score >= 90):
        return "VERY_SECURE"
    if (score >= 80):
        return "SECURE"
    if (score >= 70):
        return "VERY_STRONG"
    if (score >= 60):
        return "STRONG"
    if (score >= 50):
        return "AVERAGE"
    if (score >= 25):
        return "WEAK"
    return "VERY_WEAK"


try:
    while True:
        inputStr = sys.stdin.readline().split()[0]

        lowerLetterNum = 0  # 小写字母个数
        upperLetterNum = 0  # 大写字母个数
        numberNum = 0  # 数字个数
        otherCharNum = 0  # 其他字符个数

        for i in range(len(inputStr)):
            if (ord(inputStr[i]) <= ord('Z') and ord(inputStr[i]) >= ord('A')):
                upperLetterNum = upperLetterNum + 1
            else:
                if (ord(inputStr[i]) <= ord('z') and ord(inputStr[i]) >= ord('a')):
                    lowerLetterNum = lowerLetterNum + 1
                else:
                    if (ord(inputStr[i]) <= ord('9') and ord(inputStr[i]) >= ord('0')):
                        numberNum = numberNum + 1
                    else:
                        otherCharNum = otherCharNum + 1

        strLengthScore = getPasswordLengthScore(inputStr)  # 长度得分
        letterScore = getPasswordLetterScore(lowerLetterNum, upperLetterNum)  # 含有大小写字母得分
        numberScore = getPasswordNumberScore(numberNum)  # 含有数字大小得分
        otherCharScore = getPasswordOtherCharNumScore(otherCharNum)  # 含有其他特殊字符的得分
        extraRewardScore = getExtraRewardScore(lowerLetterNum, upperLetterNum, numberNum, otherCharNum)  # 额外得分

        totalScore = strLengthScore + letterScore + numberScore + otherCharScore + extraRewardScore
        print(getTargetLevelByScore(strLengthScore + letterScore + numberScore + otherCharScore + extraRewardScore))

except:
    pass


























