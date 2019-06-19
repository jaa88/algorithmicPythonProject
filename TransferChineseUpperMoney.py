
#  人民币转换
# 1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。（30分）
#
# 2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，如￥ 532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。（30分）
#
# 3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，如￥6007.14，应写成“人民币陆仟零柒元壹角肆分“。（

# 输入：
# 输入一个double数
# 输出
# 输出人民币格式
# 例：
# 输入 151121.15
# 输出 人民币拾伍万壹仟壹佰贰拾壹元壹角伍分

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

upperChineseNum=("壹","贰","叁","肆","伍","陆","柒","捌","玖")
underThousandNumType=("仟","佰","拾","")


def getUpperChineseNumUnderTenThousand(num):
    targetNum = num.lstrip("0")
    targetNumLength = len(targetNum)
    returnStrArr = []
    needAppendZeroflag = True
    for i in range(targetNumLength):
        if (targetNum[i] != '0'):
            needAppendZeroflag = True
            if (int(targetNum[i]) == 1 and (i + 4 - targetNumLength) == 2):
                returnStrArr.append(underThousandNumType[i + 4 - targetNumLength])
            else:
                returnStrArr.append(
                    (upperChineseNum[int(targetNum[i]) - 1]) + (underThousandNumType[i + 4 - targetNumLength]))
        else:
            if needAppendZeroflag and i != targetNumLength - 1 and followNumHasNoZero(
                    targetNum[i + 1:int(targetNumLength)]):
                needAppendZeroflag = False
                returnStrArr.append("零")
            else:
                needAppendZeroflag = True
    return "".join(returnStrArr)


def followNumHasNoZero(numStr):
    for i in numStr:
        if (i != '0'):
            return True
    return False

try:
    while True:
        num = sys.stdin.readline()

        numArr = num.split(".")

        intNum = numArr[0] + ""
        decimalNum = numArr[1] + ""


        resultStrArr = ["人民币"]
        if (len(intNum) > 8):
            if (intNum[-8] != '0' and intNum[-9] != '0'):
                resultStrArr.append(getUpperChineseNumUnderTenThousand(intNum[:-8]) + "亿")
            else:
                resultStrArr.append(getUpperChineseNumUnderTenThousand(intNum[:-8]) + "亿零")
        if (len(intNum) > 4):
            if (intNum[-4] != '0' and intNum[-5] != '0'):
                resultStrArr.append(getUpperChineseNumUnderTenThousand(intNum[-8:-4]) + "万")
            else:
                resultStrArr.append(getUpperChineseNumUnderTenThousand(intNum[-8:-4]) + "万零")
        resultStrArr.append(getUpperChineseNumUnderTenThousand(intNum[-4:]))

        # 没有角和分
        if decimalNum == "00":
            resultStrArr.append("元整")
        else:
            if (int(intNum) != 0):
                resultStrArr.append("元")
            # 角
            if(int(decimalNum[0])!=0):
                resultStrArr.append(upperChineseNum[int(decimalNum[0]) - 1] + "角")
            # 分
            if(int(decimalNum[1])!=0):
                resultStrArr.append(upperChineseNum[int(decimalNum[1]) - 1] + "分")

        print("".join(resultStrArr))
except:
    pass















