'''
68244 KB	440 ms
확실한 부분을 먼저 초기화해두고, 연산해가면서 append로 추가해가는 식으로
했었지만 100%에서 틀렸습니다가 출력된다.
아마 시간제한으로 인한 오답인 듯 하다.
완전한 dp로 구현하니 이상없이 정답이 나온다.
'''

import sys

input = sys.stdin.readline

n = int(input())
# dp = [1, 2]
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    # dp.append((dp[i-2] % 15746 + dp[i-1] % 15746) % 15746)
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])
