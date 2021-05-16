import sys


def dfs(node, Edges, startNode):
    answer = []

    return answer


def bfs(node, Edges, startNode):
    answer = []

    return answer


input = sys.stdin.readline
nodeCount, EdgeCount, startNode = list(map(int, input().strip().split()))

node = [i for i in range(1, nodeCount + 1)]
Edges = [list(map(int, input().strip().split())) for _ in range(EdgeCount)]
