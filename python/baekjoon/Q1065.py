'''
29200 KB    72 ms
'''

import sys

input = sys.stdin.readline


def isHan(n: int) -> bool:
    if n < 10:
        return True
    else:
        strN = str(n)
        flag = True
        diff = int(strN[0]) - int(strN[1])
        for i in range(1, len(strN)-1):
            if diff != int(strN[i]) - int(strN[i+1]):
                return False
        return True


n = int(input())
result = 0
for i in range(1, n+1):
    if isHan(i):
        result += 1

print(result)
