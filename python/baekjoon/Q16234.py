'''
차이가 L과 R 사이의 수만큼 나는 경우
하나의 '연합'으로 묶여야 한다.
bfs로 할 경우 queue를, dfs로 할 경우 stack을 사용하게 되는데
이 때, 들어가는 원소를 하나로 묶이는 '연합'의 단위로 넣는다.
그 연합에 들어간 경우 '하루'간 국경을 열고 인구 이동을 시작한다.
각각의 나라의 인구는 평등하게 분배되어 각 나라의 인원이
(총 인구) // (연합국가 수) 와 같은 소수점을 버리는 '평균'이 된다.

1달만에 새로 풀어봄
약간 코드에 변형을 줘서 bfs 함수 내부가 아닌 union을 구성하고 나서 인구수를 초기화 시켜주었다.
이후 python이 아닌 pypy로 제출하니 정답

일단 맞춘 후 다른 답들을 봤는데 아이디어 자체는 비슷비슷한 듯 한데.. 왜 난 시간초과지

146860 KB	1476 ms
'''

import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(contries:list, visited:list, n:int, l:int, r:int, y:int, x:int):
  global queue
  queue.append((y, x))
  union = []
  union.append((y, x))
  
  while queue:
    curY, curX = queue.popleft()
    for i in range(4):
      nY = curY + dy[i]
      nX = curX + dx[i]
      if 0 <= nX < n and 0 <= nY < n and visited[nY][nX] == 0 and l <= abs(contries[nY][nX] - contries[curY][curX]) <= r:
        visited[nY][nX] = 1
        queue.append((nY, nX))
        union.append((nY, nX))
  return union
  

n, l, r = map(int, input().strip().split())

contries = [list(map(int, input().strip().split())) for _ in range(n)]

days = 0

while True:
  visited = [[0] * n for _ in range(n)]

  flag = False
  for i in range(n):
    for j in range(n):
      avg = 0
      if visited[i][j] == 0:
        visited[i][j] = 1
        union = bfs(contries, visited, n, l, r, i, j)
        if len(union) > 1:
          flag = True
          for u in union:
            avg += contries[u[0]][u[1]]
          
          avg //= len(union)
          
          for u in union:
            contries[u[0]][u[1]] = avg
  
  # print('------------------')
  # for a in contries:
  #   print(a)
  
  if not flag:
    break
  days += 1

print(days)

''''''''''''''''''''''''''''''''''''''''''''''''''''''

# def bfs(contries:list, visited:list, n:int, l:int, r:int, y:int, x:int):
#   global cnt
#   union = []
#   sumU = contries[y][x]
#   uCnt = 0
#   global queue
#   queue.append((y, x))
#   while queue:
#     curY, curX = queue.popleft()
#     union.append((curY, curX))
#     uCnt += 1
#     visited[curY][curX] = 1

#     for i in range(4):
#       nY = curY + dy[i]
#       nX = curX + dx[i]
#       if n <= nY < 0 or n <= nX < 0 or visited[nY][nX] == 1:
#         continue
#       if l > abs(contries[curY][curX] - contries[nY][nX]) > r:
#         continue
#       queue.append((nY, nX))
#       sumU += contries[nY][nX]
#       visited[nY][nX] = 1
  
#   avgU = sumU // uCnt

#   if uCnt == 1:
#     return False
#   else :
#     for u in union:
#       contries[u[0]][u[1]] = avgU
#     return True

#   # if len(union) != 1 :
#   #   union.append(sumU // len(union))
#   # else:
#   #   union = []
#   # return union

# input = sys.stdin.readline

# n, l, r = map(int, input().split())

# contries = [list(map(int, input().split())) for _ in range(n)]

# days = 0
# flag = True

# while True:
#   visited = [[0] * n for _ in range(n)]
#   if not flag:
#     print(days)
#     break

#   for i in range(n):
#     for j in range(n):
#       if visited[i][j] == 1:
#         continue
#       flag = bfs(contries, visited, n, l, r, i, j)
#   days += 1

''''''''''''''''''''''''''''''''''''''''''''''''''''''

# while True:
#   unions = []
#   visited = [[0] * n for _ in range(n)]
#   for i in range(n):
#     for j in range(n):
#       if visited[i][j] == 1:
#         continue
#       bfs(contries, visited, n, l, r, i, j)
      # result = bfs(contries, visited, n, l, r, i, j)
      # if result:
      #   unions.append(result)
      # unions.append(bfs(contries, visited, n, l, r, i, j))

  # if not unions:
  #   # print("last", days)
  #   print(days)
  #   break

  # print("1")
  # for u in unions:
  #   print(u)

  # for u in unions:
  #   avgU = u.pop()
  #   for ua in u:
  #     contries[ua[0]][ua[1]] = avgU

  # days += 1

  # for c in contries:
  #   print(c)
  # print("-----------")

