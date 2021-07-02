# brute force
'''
29200 KB	72 ms
Q3040과 같은 문제인듯
'''
import sys
input = sys.stdin.readline

shorts = [int(input()) for _ in range(9)]

diff = sum(shorts) - 100


def sol(shorts: list, diff: int):
    for i in range(9):
        for j in range(i+1, 9):
            if shorts[i] + shorts[j] == diff:
                shorts.remove(shorts[j])
                shorts.remove(shorts[i])
                print('\n'.join(map(str, sorted(shorts))))
                return


sol(shorts, diff)
