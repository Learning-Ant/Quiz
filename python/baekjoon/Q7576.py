'''
bfs or dfs를 할 땐 visited를 적극 활용하도록 한다.
추가적으로 개선할 점은

1. start 지점들을 정함에 있어서 input을 받을 때 바로
list를 만들어 queue에 삽입하는 방법을 고려해 볼 것.
2. 아직 bfs를 따로 함수로 만드는 방법이 쉽지 않게 느껴진다.
가급적 함수로 구현할 생각부터 해볼 것.

154612 KB	3092 ms
'''

import sys
from collections import deque

direction = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]


input = sys.stdin.readline

x, y = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(y)]
visited = [[0] * x for _ in range(y)]

# for i in range(y):
#     print(field[i])

start, days = [], 0


queue = deque()
for i in range(y):
    for j in range(x):
        if field[i][j] == 1:
            start.append((i, j))

# print(start)

if start != 0:
    queue.append(start)
    while queue:
        flag = 0
        cur = queue.popleft()  # list type
        nextList = []
        for c in cur:
            for d in direction:
                nextY = c[0] + d[0]
                nextX = c[1] + d[1]
                if 0 <= nextY < y and 0 <= nextX < x and field[nextY][nextX] == 0 and visited[nextY][nextX] != 1:
                    nextList.append((nextY, nextX))
                    visited[nextY][nextX] = 1

        if nextList:
            queue.append(nextList)

        for c in cur:
            if field[c[0]][c[1]] == 0:
                field[c[0]][c[1]] = 1
                flag = 1

        if flag == 1:
            days += 1

        # for i in range(y):
        #     print(field[i])

        # print('--------------')

for i in range(y):
    if 0 in field[i]:
        days = -1

print(days)
