'''

'''

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
n, s = map(int, input().strip().split())

k = list(map(int, input().strip().split()))

def bt(a, b, c, d):
    if a == b:
        c += 1
        return
    elif a < b:
        return
    for i in d:
        a += i
        bt(a, b, c, d)
        a -= i

cnt = 0
bt(0, s, cnt, k)

print(cnt)