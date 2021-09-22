import sys


def check(x, y, _map, d, v):
    nd = 3 if d < 0 else d - 1



def dfs(x, y, _map, d, cnt):
    return


input = sys.stdin.readline
n, m = map(int, input().strip().split())
x, y, d = map(int, input().strip().split())
_map = [list(map(int, input().strip().split())) for _ in range(n)]
cnt = 0
v = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# dfs(x, y, _map, d, cnt, v)

print(cnt)
