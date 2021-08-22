'''
dfs + dp
지금은 dp를 사용하지 않은 코드..
dp를 사용하려면 어디서 memoization을 실행해야 할까
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

y, x = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(y)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

# 못 가는 지점 : 0, 방문하지 않은 지점 : -1
dp = [[-1] * x for _ in range(y)]


def dfs(curY:int, curX:int, field:list, h:int, w:int, dp:list):
  if curY == (h - 1) and curX == (w - 1):
    # print("도착")
    return 1
  if dp[curY][curX] != -1 :
    # print("memo")
    return dp[curY][curX]

  ans = 0
  for i in range(4):
    nY = curY + dy[i]
    nX = curX + dx[i]
    # print(nY, nX)
    if 0 > nY or nY >= h or 0 > nX or nX >= w :
      continue
    if field[curY][curX] > field[nY][nX] :
      ans += dfs(nY, nX, field, h, w, dp)
  
  return ans

print(dfs(0, 0, field, y, x, dp))
print(dp)

  
