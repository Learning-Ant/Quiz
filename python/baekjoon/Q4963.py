'''
BOJ 7576번 풀었을 때 bfs 함수를 따로 만들어 푸는 것에 대해 좀 어려움을 느꼈다.
이번에는 bfs 함수를 따로 선언해 풀어봤는데, 역시 parameter들이 너무 너저분한 느낌이 든다.
다른 풀이들을 보니 interpreter 언어의 특성을 이용해 w, h 값만을 paramter로 풀어낸
풀이가 꽤 많았다.

다른 풀이들을 보니 이 경우에는 dfs가 bfs보다 더 빠른 결과를 보였는데, 이유를 잘 모르겠다.
예전에 풀었던 기억에 bfs이 dfs보다 빨랐던 기억이 있었는데 이 경우는 어떻게 다른 경우인지
좀 알아봐야 할 듯 하다.

31780 KB	132 ms
'''


import sys
from collections import deque

input = sys.stdin.readline


def bfs(_map, h, w, totH, totW, visited):
    queue = deque()

    direction = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1]
    ]
    queue.append((h, w))
    visited[h][w] = 1
    while queue:
        h, w = queue.popleft()
        for d in direction:
            nextH = h + d[0]
            nextW = w + d[1]

            if 0 <= nextH < totH and 0 <= nextW < totW and visited[nextH][nextW] == 0 and _map[nextH][nextW] == 1:
                queue.append((nextH, nextW))
                visited[nextH][nextW] = 1


while True:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break

    visited = [[0] * w for _ in range(h)]
    _map = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if _map[i][j] == 1 and visited[i][j] == 0:
                bfs(_map, i, j, h, w, visited)
                cnt += 1
    print(cnt)
