'''
재귀적으로도 가능하지만 dp를 사용하는 것이 좀 더 직관적

36252 KB	748 ms
'''

import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

lenA, lenB = len(a), len(b)
# print(lenA, lenB)

dp = [[0] * (lenA + 1) for _ in range(lenB + 1)]

for i in range(1, lenB + 1):
  for j in range(1, lenA + 1):
    # print('-------- i:', i, ', j:', j, '--------')
    if a[j-1] == b[i-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else :
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    # for k in dp:
    #   print(k)

for i in dp:
  print(i)

print(dp[lenB][lenA])