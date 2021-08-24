import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))

coinCnt = 0

for i in range(n-1, -2, -1):
  if k == 0:
    print(coinCnt)
    break
  coinCnt += (k // coins[i])
  k %= coins[i]
  # print(k)