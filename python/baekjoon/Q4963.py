import sys
from collections import deque

input = sys.stdin.readline


def bfs(_map, h, w, totH, totW):
    cnt = 0
    queue = deque()
    visited = [[0] * totW for _ in range(totH)]
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
    while queue:
        h, w = queue.popleft()
        for d in direction:
            nextH = h + d[0]
            nextW = w + d[1]
            if 0 <= nextH < totH and 0 <= nextW < totW and visited[nextH][nextW] == 0 and _map[nextH][nextW] == 0:
                queue.append((nextH, nextW))
                cnt += 1
            print(cnt)

    return cnt


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    _map = []
    #start = (0, 0)
    for i in range(h):
        _mapH = list(map(int, input().split()))
        if 1 in _mapH:
            j = _mapH.index(1)
            start = (i, j)
        _map.append(_mapH)

    print(_map)
    print(start)

    print(bfs(_map, start[0], start[1], w, h))
