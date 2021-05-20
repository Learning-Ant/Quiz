import sys
input = sys.stdin.readline
n = int(input().strip())
_list = [0] * 10001
for i in range(n):
    m = int(input())
    _list[m] += 1

for i in range(len(_list)):
    if _list[i]:
        for _ in range(_list[i]):
            print(i)
