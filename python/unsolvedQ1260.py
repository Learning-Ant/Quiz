import sys


def dfs(graph, startNode):
    visited = []
    stack = [startNode]

    while stack:
        curNode = stack.pop()
        if curNode not in visited:
            visited.append(curNode)
            stack.extend(graph[curNode])

    return visited


def bfs(graph, startNode):
    answer = []

    return answer


input = sys.stdin.readline
nodeCount, EdgeCount, startNode = list(map(int, input().strip().split()))

graph = [[] for _ in range(nodeCount + 1)]
for _ in range(EdgeCount):
    s, e = map(int, input().strip().split())
    graph[s].append(e)
    graph[e].append(s)

print(graph)
dfsResult = dfs(graph, startNode)

print(dfsResult)
