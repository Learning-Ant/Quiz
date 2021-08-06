'''
138540 KB	488 ms
'''

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def dfs(n, parent, tr: list):
    for i in tr[n]:
        if parent[i] == 0:
            parent[i] = n
            dfs(i, parent, tr)


v = int(input())

tr = [[] for _ in range(v+1)]
parent = [0] * (v+1)

for _ in range(v - 1):
    a, b = map(int, input().split())
    tr[a].append(b)
    tr[b].append(a)

dfs(1, parent, tr)

print('\n'.join(list(map(str, parent[2:]))))
