import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().strip().split())

cards = list(map(int, input().strip().split()))

nCr = itertools.combinations(cards, 3)

answer = 0
for i in nCr:
    if answer < sum(i) <= m:
        answer = sum(i)

print(answer)
