from numpy.core.fromnumeric import transpose
import numpy as np
cStr = "Let it be!" * 3

print(cStr.find("it", 25, -11))
# find(string, start, end)-> 없으면 -1

# Padding

# print("우측 맞춤 : '%05d'" % 25)
# print("좌측 맞춤 : '%-05d'" % 1)
# print("우측 맞춤 : '%12.3f'" % 3.1415926535)
# print("좌측 맞춤 : '%-9.6f'" % 3.1415926535)

# print("우측 맞춤 : '{0:>10.3f}'".format(3.14159))
# print("좌측 맞춤 : '{0:.<10.3f}'".format(3.1415926))
# '11'.zfill(5)  # zero fill
# '11'.rjust(5)  # 우측 정렬, 채울 문자 지정가능(두번째 파라미터)
# '11'.ljust(5)  # 좌측 정렬, 채울 문자 지정가능(두번째 파라미터)

# open방법
# 1. f = open('filename', options...)           -> close필요
# 2. with open('filename', options...) as f:    -> 자동 close

# read는 현재 읽는 위치부터 끝까지?

f = open('test.txt', 'r')

# print(f.read())
# print(f.readline())
# li = [i.strip() for i in f.readlines(3)]
# print(li)
# options : hint
# if the number of bytes returned exceed the hint number
# no more lines will be returned
# 기준이 bytes임에 주의하자

yesterday = f.readlines()
f.close()


A = np.random.randint(1, 10, size=(3, 2))
B = np.random.randint(1, 10, size=(4, 2))

B.transpose()
C = A.dot(B.transpose())
print(C)
count = 3
for i in range(10):
    count = (count-1) % 4
    print(count)
print(-5 % 4)
