'''
32124 KB	1432 ms
'''
import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs(field:list, visited:list, precipitation:int, y:int, x:int, n:int):
  queue = deque()
  queue.append((y, x))
  while queue:
    curY, curX = queue.popleft()
    visited[curY][curX] = 1
    for i in range(4):
      nextY = curY + dy[i]
      nextX = curX + dx[i]
      if 0 <= nextY < n and 0 <= nextX < n and visited[nextY][nextX] == 0 and field[nextY][nextX] > precipitation :
        queue.append((nextY, nextX))
        visited[nextY][nextX] = 1



n = int(input())

field = [list(map(int, input().split())) for _ in range(n)]

# maxH = max(map(max, field))
# minH = min(map(min, field))

answer = 0
for p in range(100) : # or range(minH - 1, maxH + 1)
  cnt = 0
  visited = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if field[i][j] > p and visited[i][j] == 0:
        bfs(field, visited, p, i, j, n)
        cnt += 1

  answer = max(answer, cnt)

print(answer)