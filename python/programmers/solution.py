
x1 = [2, 4, 6]
x2 = [1, 3, 5]
x3 = [9, 8, 7]

y1, y2, y3 = zip(x1, x2, x3)

print(y1, y2, y3)
nSum = [sum(x) for x in zip(y1, y2, y3)]
print(nSum)

dA, dB, dC = input("계수 a, b, c 입력 >>>").split()
print(dA, dB, dC)
