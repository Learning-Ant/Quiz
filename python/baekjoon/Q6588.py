'''
에라토스테네스의 체를 활용해 먼저 소수목록을 뽑은 후
입력으로 주어진 수에 대해 가장 먼저 소수인지 판단하고,
그를 뺀 수가 소수인지 추가적으로 판단해
출력으로 결과 도출
여기서 추가적으로 도입할 수 있는 부분은 에라토스테네스의 체를 활용 할 때,
전체 범위가 아닌 전체 값의 제곱근까지만 판단하면 된다는 것.

적용하게 된다면 #1 부분에서 range(2, int(maxN**0.5) + 1)로 변경할 수 있다.

37012 KB	828 ms
'''

import sys
input = sys.stdin.readline

maxN = 1000000

primes = [1] * (maxN + 1)

primes[0], primes[1] = 0, 0

#1 에라토스테네스의 체
for i in range(2, maxN + 1):
  if primes[i] == 1:
    for j in range(i * 2, maxN + 1, i):
      if j > maxN :
        break
      primes[j] = 0

while True:
  answer = int(input())
  flag = False  # 매칭되는 값이 있었는지 판단하는 flag
  if answer == 0:
    break
  
  for i in range(2, maxN + 1):
    if primes[i] == 1 and primes[answer - i] == 1:
      # print(answer, "=", i, "+", answer - i)
      print("{} = {} + {}".format(answer, i, answer - i))
      flag = True
      break

  if not flag:
    print("Goldbach's conjecture is wrong.")

