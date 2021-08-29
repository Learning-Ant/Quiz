'''
먼저 받은 문자열들을 길이 순으로 정렬한다.
그리고 가장 긴 문자열의 가장 앞에 있는 문자에 가장 큰 숫자를 부여한다.
차례로 숫자가 부여되지 않은 문자가 나오면 그 다음 큰 숫자를 부여하고,
이미 부여된 숫자라면 부여된 숫자를 사용한다.
'''


import sys

input = sys.stdin.readline

chars = [-1] * (92) # 대문자만

n = int(input())
wordList = sorted([''.join(input().split()) for _ in range(n)], key=len, reverse=True)
# wordLength = [ len(i) for i in wordList ]

# print(n)
# print(wordList)
# print(wordLength)

curN = 9

for word in wordList:
  for w in word:
    if chars[ord(w)] == -1:
      chars[ord(w)] = curN
      curN -= 1

ans = 0

print(chars)