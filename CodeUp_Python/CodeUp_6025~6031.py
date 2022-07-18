# Python 기초 100제 [기초-값 변환/출력 변환] - 6025~6031번

#6025 - 정수 2개 입력받아 합 계산하기
a,b = input().split()
c = int(a) + int(b)
print(c)

#6026 - 실수 2개 입력받아 합 계산하기
a = input()
b = input()
c = float(a) + float(b)
print(c)

#6027 - 10진 정수 입력받아 16진수로 출력하기1
a = input()
n = int(a) # 입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'%n)

#6028 - 10진 정수 입력받아 16진수로 출력하기2
a = input()
n = int(a)
print('%X' %n)

#6029 - 16진 정수 입력받아 8진수로 출력하기
a = input()
n = int(a, 16) # 입력받은 a를 16진수로 인식해서 n에 저장
print('%o' %n)

#6030 - 영문자 1개 입력받아 10진수로 변환하기
n = ord(input()) # 입력받은 문자를 10진수 유니코드 값으로 변환 후 n에 저장
                 # ex) ord(c) : 문자 c를 10진수로 변환한 값
print(n)

#6031 - 정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c)) # c에 저장된 정수 값을 유니코드 문자로 바꿔서 출력



