import sys

input = sys.stdin.readline

n = int(input().strip())

nums = list(map(int, input().strip().split()))

answer = [-1 for _ in range(n)]

stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)

for i in answer:
    print(i, end=" ")
