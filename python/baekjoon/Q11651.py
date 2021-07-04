'''
57672 KB	508 ms
'''
import sys
input = sys.stdin.readline

n = int(input())
coord = sorted([list(map(int, input().split()))
                for _ in range(n)], key=lambda x: (x[1], x[0]))
for i in range(n):
    print(' '.join(list(map(str, coord[i]))))
