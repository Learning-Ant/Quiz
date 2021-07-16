'''
처음 n = 1인 경우를 생각하지 못해 에러 발생
가장 최소한의 경우만 직접 초기화하고 dp를 진행해야한다.

29200 KB	76 ms
'''

import sys
input = sys.stdin.readline
stairCnt = int(input())
stairScr = [int(input()) for _ in range(stairCnt)]
dp = [0]*(stairCnt+1)
dp[1] = stairScr[0]

for i in range(2, stairCnt+1):
    if (i < 2):
        dp[i] = stairScr[i-1]
    else:
        dp[i] = max(dp[i-2] + stairScr[i-1], dp[i-3] +
                    stairScr[i-2] + stairScr[i-1])

print(dp[stairCnt])
