# 记负均正2
# 从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值

# 输入：
# 输入任意个整数
# 输出
# 输出负数个数以及所有非负数的平均值
# 例：
# 输入
# -13
# -4
# -7
# 输出
# 3
# 0.0
import sys

for line in sys.stdin:
    intputStrArr = line.split()

    negativeTotalNum=0
    positiveTotalNum=0
    positiveSum=0

    for numStr in intputStrArr:
        num=int(numStr)
        if(num<0):
            negativeTotalNum+=1
        else:
            positiveSum+=num
            positiveTotalNum+=1

    print(negativeTotalNum)
    if(positiveTotalNum>0):
        print(round(positiveSum/positiveTotalNum,1))
    else:
        print(0)




