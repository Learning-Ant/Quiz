import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 5, 20

tl = sorted(list(map(int, input().split())))
# 4 26 40 42 46

iniH, finH = tl[0], tl[-1]
print(iniH, finH)
resultH = finH
print(resultH)
diffsum = 0

# while diffsum != m:
if diffsum > m:
    iniH = (iniH + finH) // 2
    resultH = iniH
elif diffsum < m:
    finH = (iniH + finH) // 2
    resultH = finH

diffsum = sum(list(map(lambda x: x - resultH if x >= resultH else 0, tl)))
print(diffsum)
print(resultH)

# print(resultH)
