import sys

input = sys.stdin.readline

v, e = map(int, input().strip().split())
sNode = int(input().strip())
# edge (from, to, weight)
eList = [tuple(map(int, input().strip().split())) for _ in range(e)]

eMap = []

# for i in range(e):