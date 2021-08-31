import sys

input = sys.stdin.readline

n = int(input().strip())

wines = [int(input().strip()) for _ in range(n)]

dp = [0] * (n + 1)
dp[1] = wines[0]

for i in range(2, n + 1):
  dp[i] = max(dp[i - 2] + wines[i - 1], dp[i - 3] + wines[i - 2] + wines[i - 1], dp[i - 1])

print(dp)
print(dp[n])