# -- coding: utf-8 --
# 现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；
# 每种砝码对应的数量为x1,x2,x3...xn。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
#
#
# 注：
#
# 称重重量包括0
#
#
# 方法原型：public static int fama(int n, int[] weight, int[] nums)
# 输入描述:
# 输入包含多组测试数据。
#
# 对于每组测试数据：
#
# 第一行：n --- 砝码数(范围[1,10])
#
# 第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])
#
# 第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
# 输出描述:
# 利用给定的砝码可以称出的不同的重量数
#
# 示例1
# 输入
# 复制
# 2
# 1 2
# 2 1
# 输出
# 复制
# 5
while True:
    try:
        #砝码的数量
        fm_num=int(input())
        #每个砝码的重量
        fm_weiths=list(map(int,input().split()))
        #每种重量砝码的数量
        per_weight_num=list(map(int,input().split()))
        '''
        思路：首先将所有的砝码放入一个listA,定义一个可称重的listB,遍历A，拿B中的每个可称重数量加当期砝码重量，结果放入listB，取最终的set
        '''
        list_a,list_b,temp=[],[0],[]
        # 将所有的砝码都放入listA中
        for i in range(fm_num):
            for j in range(per_weight_num[i]):
                list_a.append(fm_weiths[i])
        for i in list_a:
            temp=set(list_b)
            for j in temp:
                list_b.append(j+i)
        print(len(set(list_b)))
    except:
        break



















