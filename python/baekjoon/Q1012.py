def dfs():

    return


tc = int(input())
r, c, n = map(int, input().split())

field = [[0] * c for _ in range(r)]

for _ in range(n):
    x, y = map(int, input().split())
    field[x][y] = 1

dir = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]


for i in field:
    print(i)
