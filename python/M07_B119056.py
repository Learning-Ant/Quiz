# M07 python 과제

# Lab-06-01 단어 숫자 세기

# 파일 스트림 오픈
f = open('yesterday_beatles.txt', 'r')
count = 0

# 한 줄씩 읽으면서 개수 카운팅
while True:
    line = f.readline().replace(',', '')
    count += line.lower().count('yesterday')
    if not line:
        break

# 파일 스트림 닫기
f.close()
print('찾는 단어({})는 총 {}개 있습니다.'.format('yesterday', count))

# Lab-06-02 File Write & Read
f = open('TestFile_01.txt', 'w')

# 'TestFile_01.txt'에 기록하기
f.write("         Web Programming 2019 by Prof.Jhee\n")
f.write("          Python Programming for Data Analytics\n")
f.write("Python is an awesome programming lanuage. It's simple and easy to learn. I can do it!!!\n\n")
f.write("   파이썬은 Big Data/AI 시대의 필수적인 프로그래밍 언어로 자리 잡았으며 Goggle의 기본 개발언어로 사용되고 있습니다.\n")
f.write("여러분도 파이썬을 잘 익혀서 4차 산업혁명의 역군이 되기를 바랍니다.\n\n")
f.write(" 3.14 36 18.2 \'data science\' 256 \'999\' 55 ")

# file stream close
f.close()

# file streams open
f1 = open('TestFile_01.txt', 'r')
f2 = open('TestFile_02.txt', 'w')

# 한 줄씩 읽어가면서 각각 변환시켜 'TestFile_02.txt'에 출력
while True:
    line = f1.readline()
    if not line:
        break
    f2.write(line.strip()+'\n')
    f2.write(line.strip().upper()+'\n')
    f2.write(line.strip().replace(' ', '-')+'\n')

# file streams close
f1.close()
f2.close()
