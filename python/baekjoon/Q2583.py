'''
단순한 그래프 탐색 문제

31896 KB	128 ms
'''

import sys
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs(visited:list, y:int, x:int, h:int, w:int)->int:
  cnt = 0
  queue = deque()
  queue.append((y,x))

  while queue:
    curY, curX = queue.popleft()
    visited[curY][curX] = 1
    cnt += 1
    
    for i in range(4):
      nY = curY + dy[i]
      nX = curX + dx[i]
      if 0 <= nY < h and 0 <= nX < w and visited[nY][nX] == 0:
        queue.append((nY, nX))
        visited[nY][nX] = 1

  return cnt


input = sys.stdin.readline

y, x, k = map(int, input().split())

coords = []

for _ in range(k):
  coords.append(tuple(map(int, input().split())))

visited = [[0] * x for _ in range(y)]

while coords:
  ix, iy, fx, fy = coords.pop()
  for i in range(iy, fy):
    for j in range(ix, fx):
      if visited[i][j] == 1:
        continue
      visited[i][j] = 1

answer = []

for i in range(y):
  for j in range(x):
    if visited[i][j] == 0 :
      answer.append(bfs(visited, i, j, y, x))

# for i in visited:
#   print(i)

print(len(answer))
print(" ".join(list(map(str, sorted(answer)))))