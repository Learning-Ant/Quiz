'''
풀긴했지만 Pythonic Coding은 하지 못한 문제
마지막 list 값에 접근할 때 -1을 사용할 수 있다는 점.
if로 경우를 나눌 필요없이 첫번째와 마지막값은 무조건 윗 열에서 더하는 경우가 하나밖에 없다는 점
따라서 if로 할 필요없이 inner loop에서 2부터 i-1까지만 돌면 된다는 것.
여러모로 문제의 풀이에만 집중한 것이 문제.

38320 KB	196 ms
'''

import sys
input = sys.stdin.readline

floorCnt = int(input())
tri = []

for _ in range(floorCnt):
    tri.append(list(map(int, input().split())))

dp = [[0] * (i+1) for i in range(floorCnt)]
dp[0][0] = tri[0][0]

for i in range(1, len(tri)):
    n = len(dp[i])
    for j in range(n):
        if j == 0:
            dp[i][j] = tri[i][j] + dp[i-1][0]
        elif j == n-1:
            dp[i][j] = tri[i][j] + dp[i-1][n-2]
        else:
            dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[len(tri)-1]))
