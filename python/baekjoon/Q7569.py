'''
7576번 + 차원수만 높아진 문제
이전에 풀었던 문제에서 z차원만 추가된 유형이다.
일단 다른 풀이가 생각나지 않아 전과 같은 방식으로 풀긴했다.

좀 더 다듬을 여지가 많아 보임.

1. 다음 성장할 tomato에 대한 List를 만들면서 동시에 해당 tomato를 성장했다고 할 방법?
2. 입력값 중 0이 없다면 bfs돌 필요가 없으므로 바로 0을 출력한 후 종료하도록 하는 방법?

66532 KB	3748 ms
'''


import sys
from collections import deque


# def printField(z, y, field):

#     for i in range(z):
#         for j in range(y):
#             print(field[i][j])
#         print('----------')


def bfs(field: list, start, visited):
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]
    queue = deque()
    queue.append(start)
    days = 0

    while queue:
        curList = queue.popleft()
        flag = 0
        nextList = []
        for cur in curList:
            curZ, curY, curX = cur
            visited[curZ][curY][curX] = 1
            for i in range(6):
                nZ = curZ + dz[i]
                nY = curY + dy[i]
                nX = curX + dx[i]
                if 0 <= nZ < z and 0 <= nY < y and 0 <= nX < x and visited[nZ][nY][nX] == 0 and field[nZ][nY][nX] == 0:
                    nextList.append((nZ, nY, nX))
                    visited[nZ][nY][nX] = 1

        for cur in curList:
            if field[cur[0]][cur[1]][cur[2]] == 0:
                field[cur[0]][cur[1]][cur[2]] = 1
                flag = 1

        if nextList:
            queue.append(nextList)
        if flag:
            days += 1

    return days


input = sys.stdin.readline

x, y, z = map(int, input().split())

start = []
visited = [[[0]*x for _ in range(y)] for _ in range(z)]

field = []

for i in range(z):
    tempZ = []
    for j in range(y):
        temp = list(map(int, input().split()))
        for k in range(x):
            if temp[k] == 1:
                start.append((i, j, k))
        tempZ.append(temp)
    field.append(tempZ)

answer = bfs(field, start, visited)

for i in range(z):
    for j in range(y):
        if 0 in field[i][j]:
            print(-1)
            exit(0)

print(answer)
