'''
29452 KB	100 ms
'''

import sys
input = sys.stdin.readline

w = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def wdp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w[20][20][20]
    else:
        return w[a][b][c]


for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                w[i][j][k] = 1
            elif i < j < k:
                w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
            else:
                w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + \
                    w[i-1][j][k-1] - w[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().strip().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, wdp(a, b, c)))
