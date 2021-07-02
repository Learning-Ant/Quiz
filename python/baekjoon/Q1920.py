# Binary Search
import sys


def binarySearch(numbers: list, target: int):
    left = 0
    right = len(numbers) - 1
    while(left <= right):
        mid = (left + right) // 2
        if numbers[mid] == target:
            print(1)
            return
        elif numbers[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(0)


input = sys.stdin.readline
input()
numbers = sorted(list(map(int, input().strip().split())))
input()
targetList = list(map(int, input().strip().split()))

for target in targetList:
    binarySearch(numbers, target)
