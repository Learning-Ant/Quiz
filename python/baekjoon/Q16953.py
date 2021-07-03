# 특정 자릿수를 탈락시키는 연산은 나누기 사용

'''
29200 KB	72 ms
'''

import sys
input = sys.stdin.readline
a, b = map(int, input().split())
count = 1
while a < b:
    if b % 2 != 0:
        b -= 1
        b /= 10
    else:
        b /= 2
    count += 1
if a == b:
    print(count)
else:
    print(-1)
