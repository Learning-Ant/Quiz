'''
29200 KB	72 ms
정렬문제
내장함수로 풀이
'''

import sys
input = sys.stdin.readline

n = int(input())
numList = sorted([int(input()) for _ in range(n)])

print('\n'.join(map(str, numList)))
