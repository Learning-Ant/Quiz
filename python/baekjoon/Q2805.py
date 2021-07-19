'''
145836 KB	4864 ms
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tl = sorted(list(map(int, input().split())))

iniH, finH = 0, tl[-1]
resultH = finH
diffsum = 0

while iniH <= finH:
    midH = (iniH + finH) // 2
    diffsum = sum(list(map(lambda x: x - midH if x >= midH else 0, tl)))
    if diffsum >= m:
        iniH = midH + 1
        resultH = midH
    elif diffsum < m:
        finH = midH - 1
print(resultH)
