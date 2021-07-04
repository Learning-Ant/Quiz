# Binary Search
'''
45008 KB	596 ms
python에는 in으로 해당 요소가 존재하는지 판단할 수 있지만,
이진 탐색의 방법을 사용해서 풀어봤다.
in으로 풀때보다 상당한 자원이 소모되는 경향을 보인다.
'''
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
