# DFS & BFS

import sys
from collections import deque


def dfs(start, visited, graph):
    visited += [start]
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and (i not in visited):
            dfs(i, visited, graph)
    return visited


def bfs(start, graph):
    queue = deque([start])
    visited = [start]

    while queue:
        i = queue.popleft()
        for j in range(len(graph[i])):
            if graph[i][j] == 1 and j not in visited:
                queue.append(j)
                visited.append(j)
    return visited


input = sys.stdin.readline

v, e, s = map(int, input().strip().split())

graph = [[0] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    edge = list(map(int, input().strip().split()))
    graph[edge[0]][edge[1]] = 1
    graph[edge[1]][edge[0]] = 1

print(*(dfs(s, [], graph)))
print(*(bfs(s, graph)))
