'''
built-in 함수인 all의 사용법
29200 KB	72 ms
'''
import sys
input = sys.stdin.readline

arr = list(map(int, input().strip().split()))
i = 0
isSorted = False
while True:
  if isSorted:
    break
    
  if arr[i] > arr[i + 1]:
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(' '.join(list(map(str, arr))))
  
  i += 1
  if i > 3 :
    i = 0

  isSorted = all(arr[j] < arr[j + 1] for j in range(len(arr) - 1))
