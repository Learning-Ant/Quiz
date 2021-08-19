'''
벽의 위치에 따라 안전구역과 오염구역이 나뉘게 된다.
안전구역이 최대가 되는 벽의 위치를 바로 판단할 방법이 없다.
즉, brute force + dfs(bfs) 로 풀어야 한다는 의미

풀이중
'''

import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs(field:list, y:int, x:int, visited:list):
  n = len(field)
  cnt = 0
  queue = deque()
  queue.append((y, x))
  while queue:
    curY, curX = queue.popleft()
    cnt += 1
    for i in range(4):
      nY = curY + dy[i]
      nX = curX + dx[i]
      if 0 <= curY < n and 0<= curX < n and visited[nY][nX] == 0:
        queue.append((nY, nX))
        visited[nY][nX] = 1

y, x = map(int, input().split())

original = [list(map(int, input().split())) for _ in range(y)]

'''
배열을 copy하지 않고 벽을 저장하는 stack을 만들어서 풀어본다.
'''

walls = []
safety = 0
for i in range(y):
  for j in range(x):
    visited = [[0] * x for _ in range(y)]
    safety = max(safety, bfs(original, 0, 0, visited))
    # 벽을 세개 세웠을 때만 계산해야한다.. 으음..