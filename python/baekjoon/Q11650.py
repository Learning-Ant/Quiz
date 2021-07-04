'''
57672 KB	492 ms
'''
import sys
input = sys.stdin.readline

n = int(input())
coord = sorted([list(map(int, input().split()))
                for _ in range(n)], key=lambda x: (x[0], x[1]))
for i in range(n):
    print(' '.join(list(map(str, coord[i]))))
