import sys
input = sys.stdin.readline

n = int(input().strip())

five = n // 5
two = (n % 5) // 2

cnt = five + two

if n == (five * 5 + two * 2):
  print(cnt)
else :
  while True:
    if five == 0:
      if two * 2 != n:
        cnt = -1
      break
    five -= 1
    two 
    