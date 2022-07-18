# Python 기초 100제 [조건/선택실행구조] - 6065~6070번

#6065 - 정수 3개 입력받아 짝수만 출력하기
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
if a%2 == 0:
    print(a)
if b%2 == 0:
    print(b)
if c%2 == 0:
    print(c)

#6066 - 정수 3개 입력받아 짝/홀 출력하기
a, b, c = input().split()

if int(a) % 2 == 0:
    print("even")
else:
    print("odd")

if int(b) % 2 == 0:
    print("even")
else:
    print("odd")

if int(c) % 2 == 0:
    print("even")
else:
    print("odd")

#6067 - 정수 1개 입력받아 분류하기
n=int(input())

if n<0:
  if n%2==0:
    print('A')
  else:
    print('B')
else:
  if n%2==0:
    print('C')
  else:
    print('D')

#6068 - 점수 입력받아 평가 출력하기
n = int(input())

if n>=90:
    print('A')
elif n>=70:
    print('B')
elif n>=40:
    print('C')
else:
    print('D')

#6069 - 평가 입력받아 다르게 출력하기
c = input()

if c == 'A':
    print("best!!!")
elif c == 'B':
    print("good!!")
elif c == 'C':
    print("run!")
elif c == 'D':
    print("slowly~")
else:
    print("what?")

#6070 - 월 입력받아 계절 출력하기
n = int(input())

if 2 < n < 6:
    print("spring")
elif 5 < n < 9:
    print("summer")
elif 8 < n < 12:
    print("fall")
else:
    print("winter")

