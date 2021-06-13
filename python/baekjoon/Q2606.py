def dfs(start, visited, graph):
    visited += [start]
    for v in graph[start]:
        if v not in visited:
            dfs(v, visited, graph)

    return visited


v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(len(dfs(1, [], graph))-1)
