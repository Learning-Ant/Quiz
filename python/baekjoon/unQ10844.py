import sys
input = sys.stdin.readline

n = int(input())

dp = [[] for _ in range(n)]

dp[0].append(9)
print(dp)
for i in range(1, n):
    for j in dp[i-1]:
        dp[i].append(j)
        dp[i].append(j-1)
    print(dp[i])
    print(sum(dp[i]) % 1000000000)


print(sum(dp[n-1]) % 1000000000)
