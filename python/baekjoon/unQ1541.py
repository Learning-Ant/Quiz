calcul = input().split('-')
sum = 0

for i in range(len(calcul)):
    if calcul[i][0] == '0':
        num = eval(calcul[i][1:])
    else:
        num = eval(calcul[i])
    if i == 0:
        sum += num
    else:
        sum -= num

print(sum)
