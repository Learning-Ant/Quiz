'''
Sort + Greedy
57672 KB	488 ms
'''

import sys
input = sys.stdin.readline

n = int(input())
ls = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[1], x[0]))

# print(ls)
prev = 0
ans = [ls[0]]

for i in range(1, n):
  if ls[i][0] >= ans[-1][1]:
    ans.append(ls[i])

# print(ans)
print(len(ans))