'''
1장의 카드를 살 경우 최대 비용은 P_1
2장의 카드를 살 경우 최대 비용은 max(2*P_1, P_2)
3장 - max(3 * P_1, P_1 + P_2, P_3) -> 이미 2장을 고려했을 때 P_1 + P_1를 고려했으므로
3장의 경우 max(P_1 + P_2, P_3)만 고려하면 된다.
...
n장의 경우 총 합이 n이 되도록 하는 모든 경우의 수 중에
가장 큰 경우를 판단해야한다.
max(P_[n-m] + P_[m], P_n)
루프를 돌며 위 값들을 비교해 가장 큰 값을 가져야 한다.

29200 KB	280 ms
'''
import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0] * (n + 1)

price = [0]
price.extend(list(map(int, input().strip().split())))
# price = [0] + list(map(int, input().strip().split()))

for i in range(1, n + 1):
  for j in range(1, i + 1):
    dp[i] = max(dp[i - j] + price[j], dp[i])

print(dp[n])