'''
29200 KB	76 ms
'''

import sys
input = sys.stdin.readline

tc = int(input().strip())

dp = [0] * 12

dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 12):
  dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(tc):
  print(dp[int(input().strip())])
