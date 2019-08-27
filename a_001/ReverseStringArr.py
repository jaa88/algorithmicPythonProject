# 字符逆序
# 将一个字符串str的内容颠倒过来，并输出。str的长度不超过100个字符。 如：输入“I am a student”，输出“tneduts a ma I”。

# 输入：
# inputString：输入的字符串
# 输出
# 输出转换好的逆序字符串
# 例：
# 输入 I am a student
# 输出 tneduts a ma I

import sys

for line in sys.stdin:
    inputStr = line.strip()
    outStr = ""
    for i in range(len(inputStr)):
        outStr += inputStr[len(inputStr) - i - 1]
    print(outStr)
































