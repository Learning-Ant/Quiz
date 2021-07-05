'''
29200 KB	68 ms
'''
import sys
input = sys.stdin.readline

dp = [[1, 0], [0, 1]]

tc = int(input())
for i in range(2, 41):
    dp.append([dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]])

# print(dp)
for i in range(tc):
    n = int(input())
    print(dp[n][0], dp[n][1])
