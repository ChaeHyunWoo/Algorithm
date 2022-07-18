# Python 기초 100제 [산술연산] - 6032~6045번

#6032 - 정수 1개 입력받아 부호 바꾸기
n = int(input())
print(-n)

#6033 - 문자 1개 입력받아 다음 문자 출력하기

# n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
n = ord(input())
print(chr(n+1))

#6034 - 정수 2개 입력받아 차 계산하기
a,b = input().split()
c = int(a) - int(b)
print(c)

#6035 - 실수 2개 입력받아 곱 계산하기
f1, f2 = input().split()
m = float(f1)*float(f2)
print(m)

#6036 - 단어 여러 번 출력하기
w,n = input().split() # w는 단어 / n는 횟수
print(w * int(n))

#6037 - 문장 여러 번 출력하기
n = input()
s = input()
print(int(n) * s)

#6038 - 정수 2개 입력받아 거듭제곱 계산하기
a,b = input().split()
a=int(a)
b=int(b)
c = a ** b
print(c)

#6039 - 실수 2개 입력받아 거듭제곱 계산하기
f1,f2 = input().split()
f1 = float(f1)
f2 = float(f2)
c = f1 ** f2
print(c)

#6040 - 정수 2개 입력받아 나눈 몫 계산하기
a,b = input().split()
a = int(a)
b = int(b)
print(a//b)

#6041 - 정수 2개 입력받아 나눈 나머지 계산하기
a,b = input().split()
a = int(a)
b = int(b)
print(a%b)

#6042 - 실수 1개 입력받아 소숫점이하 자리 변환하기

# 2f를 쓰면 소수점 아래 3번째 자리에서 반올림한 값
a = float(input())
print(format(a, ".2f"))

#6043 - 실수 2개 입력받아 나눈 결과 계산하기
f1,f2 = input().split()
f1 = float(f1)
f2 = float(f2)
f3 = f1 / f2
print(format(f3, ".3f"))

#6044 - 정수 2개 입력받아 자동 계산하기
a,b = input().split()
a = int(a)
b = int(b)

plus = a+b # 합
minus = a-b # 빼기
gop = a*b # 곱셈
mok = a//b # 몫 구하기
namage = a%b # 나머지 구하기
nanun = a/b # 나누기(소수점 둘째 자리까지 출력)

print(plus)
print(minus)
print(gop)
print(mok)
print(namage)
print(format(nanun, ".2f"))

#6045 - 정수 3개 입력받아 합과 평균 출력하기
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

plus = a+b+c #합
avg = float((a+b+c)/3) #평균

print(plus, format(avg, ".2f"))

