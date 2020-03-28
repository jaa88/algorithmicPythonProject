# 有一只兔子，从出生后第3个月起每个月都生一只兔子，
# 小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，
# 问每个月的兔子总数为多少？


def get_rabbit_num(n):
    if(n==1 or n==2):
        return 1
    else:
        return get_rabbit_num(n-1)+get_rabbit_num(n-2)


while True:
    try:
        target_month = int(input())

        total_num = get_rabbit_num(target_month)

        print(total_num)
    except:
        break
