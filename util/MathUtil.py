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
    return int(a*b/maxCommonDivisor)