'''
벽의 위치에 따라 안전구역과 오염구역이 나뉘게 된다.
안전구역이 최대가 되는 벽의 위치를 바로 판단할 방법이 없다.
즉, brute force + dfs(bfs) 로 풀어야 한다는 의미

답은 나오지만 시간초과
좀 더 효율적인 방법이 필요한데 우선 생각할 수 있는 건,
1. 배열을 copy하지 않고 바이러스를 퍼뜨리는 방법
-> 현재는 bfs를 통해 바이러스를 퍼뜨리고, 이 때의 안전구역의 수를 구하고 있다.
-> 당장 생각나는 방법은 바이러스를 퍼뜨리면서 원본의 수를 바꾸지 말고, count 변수를 따로 두고 여기서 1칸씩 빼는 방법

2. bfs가 아닌 dfs를 사용?
3. temp와 ans의 max판단
-> 먼저 ans를 list로 생성하고 일단 답의 배열을 받는다?
-> 아마 경우의 수가 많아질 경우 ans에 모든 답을 저장하는 것은 좋지 않을 듯하다.
-> 이는 지금처럼 각각의 경우 더 큰 수만을 저장하는 방법이 좋을 것 같다.
'''

import sys
from collections import deque
import copy
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

ans = 0

def bfs(field:list, virusList:list, h:int, w:int):
  global ans
  cField = copy.deepcopy(field)
  visited = [[0] * w for _ in range(h)]
  queue = deque()
  
  for vY, vX in virusList:
    queue.append((vY, vX))
    while queue:
      curY, curX = queue.popleft()
      for i in range(4):
        nY = curY + dy[i]
        nX = curX + dx[i]
        if 0 <= nY < h and 0 <= nX < w and visited[nY][nX] == 0 and cField[nY][nX] == 0:
          queue.append((nY, nX))
          cField[nY][nX] = 2
          visited[nY][nX] = 1

  temp = 0
  for r in cField:
    temp += r.count(0)
  ans = max(ans, temp)

def wall(wCnt:int, virusList:list, field:list, h:int, w:int):
  if wCnt == 3:
    bfs(field, virusList, h, w)
    return
  
  for i in range(h):
    for j in range(w):
      if field[i][j] == 0:
        field[i][j] = 1
        wall(wCnt + 1, virusList, field, h, w)
        field[i][j] = 0


y, x = map(int, input().split())

original = [list(map(int, input().split())) for _ in range(y)]

virusList = []
for i in range(y):
  for j in range(x):
    if original[i][j] == 2:
      virusList.append((i, j))

wall(0, virusList, original, y, x)

print(ans)