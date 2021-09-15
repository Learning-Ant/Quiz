'''
68756 KB	596 ms
'''

import sys
input = sys.stdin.readline

tc = int(input().strip())

n = 1000001
mod = 1000000009

dp = [0] * n
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, n):
  dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % mod

for _ in range(tc):
  print(dp[int(input().strip())])