# Python 기초 100제 [반복실행구조] - 6071~6076번

#6071 - 0 입력될 때까지 무한 출력하기
while True:
    a=input()
    a=int(a)
    if a==0:
        break
    else:
        print(a)

#6072 - 정수 1개 입력받아 카운트다운 출력하기1
n = int(input())

while True:
    print(n)

    n -= 1
    if n == 0:
        break

#6073 - 정수 1개 입력받아 카운트다운 출력하기2
n = int(input())

while True:
    n -= 1
    print(n)
    if n == 0:
        break

#6074 - 문자 1개 입력받아 알파벳 출력하기
c = ord(input())
t = ord('a')
while t <= c:
    print(chr(t), end=' ')
    t += 1

#6075 - 정수 1개 입력받아 그 수까지 출력하기1
n = int(input())
count = 0
while True:
    print(count)
    count += 1
    if count > n:
        break

#6076 - 정수 1개 입력받아 그 수까지 출력하기2
n = int(input())

for i in range(n+1):
    print(i)

