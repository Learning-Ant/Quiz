import sys

input = sys.stdin.readline

testCase = int(input())
answer = []

for i in range(testCase):
    h, w, n = map(int, input().strip().split())

    floor = n % h
    num = n // h

    if floor == 0:
        floor = h
        num -= 1

    answer.append(floor * 100 + num+1)

for i in answer:
    print(i)
