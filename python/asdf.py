import time


def add(x: int, y: int) -> int:
    return x + y


print(add('이건 문자열인데 ', '더해지네..'))


def add1(a, b=4):
    return a + b


print(add1(2))


print('프로그램 시작! ', time.time())
print('함수 정의 직전 : ', time.time())


def now_time(now=time.time()):
    print(now)


print('함수 정의 직후 : ', time.time())

now_time()
now_time()
now_time()

print('함수 실행 직후 : ', time.time())


def test(x, L=[]):
    L.append(x)
    return L


print(test(1))
print(test(2))
print(test(3))


def test(x, L=None):
    if L is None:
        L = []
    L.append(x)
    return L


print(test(1))
print(test(2))
print(test(3))


def test1(a, b, c):
    return c, b, a


print(test1(c=1, b=2, a=3))


def hello(sName1, *sName2):
    print("안녕 {}! 난 {}이야!".format(sName2, sName1))


hello('도라에몽', '이슬', '퉁퉁', '비실', '진구')


def myInfo(**kwargs):
    print('이름 : ', kwargs['name'])
    print('나이 : ', kwargs['age'])
    print('거주지 : ', kwargs['address'])


myInfo(**{'name': '스폰지밥', 'age': '?', 'address': '깊은 저 바닷속'})
