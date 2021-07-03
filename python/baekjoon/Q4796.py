# L, P, V
# 현재 선택 가능한 가장 최적의 해를 선택
# days += (V // P) * L
# days += V % P
'''
29200 KB	68 ms
'''

import sys
input = sys.stdin.readline
case = []

while True:
    days = 0
    l, p, v = map(int, input().strip().split())
    if l == 0 and p == 0 and v == 0:
        break
    days += (v // p) * l
    # 남은날이 연속 숙박가능 날보다 클경우
    if v % p > l:
        days += l
    else:
        days += v % p
    case.append(days)

for i in range(len(case)):
    print("Case {}: {}".format(i+1, case[i]))
