'''
31848 KB	104 ms
사실 이 문제를 처음 풀때는 마지막 목적지까지 도달했을 때,
최소의 거리를 구해야 하므로 그를 위한 로직이 따로 필요할 것으로 생각했다.
하지만 bfs 알고리즘 특성상 이는 고려해주지 않아도 되었으며, 문제에서 도착점까지 도달하는 경로는 무조건
존재하다고 했으니 그저 bfs알고리즘의 구현만 신경쓰면 되는 문제였던 것 같다.
'''
from collections import deque


def bfs(y, x, r, c, maze):
    queue = deque()
    queue.append((y, x))
    visited = [[False] * c for _ in range(r)]
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited[y][x] = True

    while queue:
        cur = queue.popleft()
        visited[cur[0]][cur[1]] = True

        for d in dir:
            nextY = cur[0] + d[0]
            nextX = cur[1] + d[1]
            if 0 <= nextY <= r - 1 and 0 <= nextX <= c - 1 and not visited[nextY][nextX] and maze[nextY][nextX] == 1:
                maze[nextY][nextX] = maze[cur[0]][cur[1]] + 1
                queue.append((nextY, nextX))


y, x = map(int, input().strip().split())

maze = [list(map(int, input().strip())) for _ in range(y)]

bfs(0, 0, y, x, maze)

print(maze[y-1][x-1])
