'''
dp로 풀이
각 경우의 수는 이전의 합에서 작은 경우를 더해준다.
이 경우 3가지 색상이 있으므로 2차원 배열을 이용해 i번째 집에서
각각의 색상을 칠하는 경우를 모두 생각해준다.
29452 KB    72 ms
'''

import sys
input = sys.stdin.readline
hCount = int(input())
cost = []

for _ in range(hCount):
    cost.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(hCount)]
dp[0][0], dp[0][1], dp[0][2] = cost[0]
for i in range(1, hCount):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[hCount-1]))
