'''
bfs
'''

import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

monkeyDy = [0, 1, 0, -1]
monkeyDx = [1, 0, -1, 0]
horseDy = [-1, 1, 2, 2, 1, -1, -2, -2]
horseDx = [2, 2, 1, -1, -2, -2, -1, 1]

cnt = 0

def bfs(field:list, curY:int, curX:int, y:int, x:int, visited:list, horseCnt:int):
  global queue
  global cnt
  global monkeyDx
  global monkeyDy
  global HorseDx
  global HorseDy
  
  queue.append((curX, curY, cnt, horseCnt))

  while queue:
    curX, curY, cnt, horseCnt = queue.popleft()
    if horseCnt :
      for i in range(8):
        nX, nY = curX + horseDx[i], curY + horseDy[i]
        if 0 <= nX < x and 0 <= nY < y and field[nY][nX] == 0:
          '''
          horseCnt에 따라 visited 리스트에 어떻게 저장할 것 인가?
          '''
    for i in range(4):
      nX, nY = curX + monkeyDx[i], curY + monkeyDy[i]

k = int(input())
x, y = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(y)]
visited = [[[0] * (k + 1) for _ in range(x)] for _ in range(y)]