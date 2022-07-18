# Python 기초 100제 [논리 / 비트단위논리연산 / 3항 연산] - 6053~6062번

#6053 - 참 거짓 바꾸기
a = bool(int(input()))
print(not a) # 앞에 not을 쓰면 값이 반대로 나온다

#6054 - 둘 다 참일 경우만 참 출력하기
a,b = input().split()
a,b = int(a), int(b)
print(bool(int(a)) and bool(int(b)))

#6055 - 하나라도 참이면 참 출력하기
a,b = input().split()
print(bool(int(a)) or bool(int(b)))

#6056 - 참/거짓이 서로 다를 때에만 참 출력하기
a,b = input().split()
# True 혹은 False 값이 들어감
c = bool(int(a))
d = bool(int(b))

print((c and (not d) or (not c) and d))

#6057 - 참/거짓이 서로 같을 때에만 참 출력하기
a,b = input().split()
c = bool(int(a))
d = bool(int(b))
if c == d:
    print(True)
elif (not c) == (not d):
    print(True)
else:
    print(False)

#6058 - 둘 다 거짓일 경우만 참 출력하기
a,b = input().split()
c = bool(int(a))
d = bool(int(b))
if (not c) and (not d):
    print(True)
else:
    print(False)

#6059 - 비트단위로 NOT 하여 출력하기
a = int(input())
print(~a)

#6060 - 비트단위로 AND 하여 출력하기
a,b = input().split()
print(int(a)&int(b))

#6061 - 비트단위로 OR 하여 출력하기
a,b = input().split()
print(int(a)|int(b))

#6062 - 비트단위로 XOR 하여 출력하기
a,b = input().split()
print(int(a)^int(b))

#6063 - 정수 2개 입력받아 큰 값 출력하기
a,b = input().split()
a,b = int(a), int(b)
# 삼항 연산자 - x if x<y else b 형태의 조건 연산자를 의미
print(a if a>b else b)

#6064 - 정수 3개 입력받아 가장 작은 값 출력하기
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

print((b if a>b else a) if ((b if a>b else a)<c) else c)