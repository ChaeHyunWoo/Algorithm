# Python 기초 100제 [기초-출력] - 6009~6024번

# Java에서는 사용자가 입력한 값을 받기위해 대부분 Scanner를 사용했다.
# Python에서는 input()을 사용해서 사용자가 키보드로 입력한 값을 가져온다.
# 변수 = input() 을 실행시키면 키보드로 입력한 값을 왼쪽 변수에 저장함

#6009 - 문자 1개 입력받아 그대로 출력하기
c = input()
print(c)

#6010 - 정수 1개 입력받아 int로 변환하여 출력하기
n = input()
n = int(n)
print(n)

#6011 - 실수 1개 입력받아 변환하여 출력하기
f = input()
f = float(f)
print(f)

#6012 - 정수 2개 입력받아 그대로 출력하기1
a=input()
b=input()

a=int(a)
b=int(b)

print(a)
print(b)

#6013 - 문자 2개 입력받아 순서 바꿔 출력하기1
a=input()
b=input()

print(b)
print(a)

#6014 - 실수 1개 입력받아 3번 출력하기
# input()뒤에 있는 split()를 사용하면 공백을 기준으로 입력된 값들을 나누어 자른다. 공백을 두고 입력받을 때 사용
a,b = input().split()

a=int(a)
b=int(b)

print(a)
print(b)

#6015 - 정수 2개 입력받아 그대로 출력하기2
a,b = input().split()

a=int(a)
b=int(b)

print(a)
print(b)

#6016 - 문자 2개 입력받아 순서 바꿔 출력하기2
c1,c2 = input().split()

print(c2)
print(c1)

#6017 - 문장 1개 입력받아 3번 출력하기
s = input()
print(s, s, s)

#6018 - 시간 입력받아 그대로 출력하기
a,b = input().split(":")
print(a,b,sep=':')

#6019 - 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.')
print(d,m,y,sep='-')

#6020 - 주민번호 입력받아 형태 바꿔 출력하기
a,b = input().split('-')
print(a,b,sep='')

#6021 - 단어 1개 입력받아 나누어 출력하기
s = input()

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#6022 - 연월일 입력받아 나누어 출력하기
s = input()

print(s[0:2])
print(s[2:4])
print(s[4:6])

#6023 - 시분초 입력받아 분만 출력하기
a,b,c = input().split(':')
print(b)

#6024 - 단어 2개 입력받아 이어 붙이기
w1, w2 = input().split()
s = w1 + w2
print(s)

