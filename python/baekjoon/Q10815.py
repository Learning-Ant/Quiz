'''
114956 KB	2656 ms
'''

import sys

def binarySearch(numbers: list, target: int):
    left = 0
    right = len(numbers) - 1
    while(left <= right):
      mid = (left + right) // 2
      if numbers[mid] == target:
        return 1
      elif numbers[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
    return 0

n = int(input().strip())
nl = sorted(list(map(int, input().strip().split())))

m = int(input().strip())
ml = list(map(int, input().strip().split()))

ans = []

for i in ml:
  ans.append(binarySearch(nl, i))

print(' '.join(list(map(str, ans))))