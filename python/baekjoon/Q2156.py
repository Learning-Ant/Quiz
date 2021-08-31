'''
세 가지 경우를 생각한다.

1. 현재 잔을 마시지 않는 경우
  1-1. 이전 잔을 마시는 경우
  1-2. 전전잔 + 이전잔을 마시는 경우
2. 현재 잔을 마시는 경우
  2-1. 이전 잔을 마시는 경우

29708 KB	84 ms
'''

import sys

input = sys.stdin.readline

n = int(input().strip())

wines = [int(input().strip()) for _ in range(n)]

dp = [0] * (n + 1)
dp[1] = wines[0]

for i in range(2, n + 1):
  dp[i] = max(dp[i - 2] + wines[i - 1], dp[i - 3] + wines[i - 2] + wines[i - 1], dp[i - 1])

print(dp[n])