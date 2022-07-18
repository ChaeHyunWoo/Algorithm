# Python 기초 100제 [비트시프트/비교연산] - 6046~6051번

#6046 - 정수 1개 입력받아 2배 곱해 출력하기
n = int(input())
print(n<<1)

#6047 -  2의 거듭제곱 배로 곱해 출력하기
a,b = input().split()
a,b = int(a), int(b)

print(a<<b)

#6048 - 정수 2개 입력받아 비교하기1
a,b = input().split()
a,b = int(a), int(b)
if a < b:
    print(True)
else:
    print(False)

#6049 - 정수 2개 입력받아 비교하기2
a,b = input().split()
a,b = int(a), int(b)
if a == b:
    print(True)
else:
    print(False)

#6050 - 정수 2개 입력받아 비교하기3
a,b = input().split()
a,b = int(a), int(b)
if a <= b:
    print(True)
else:
    print(False)

#6051 - 정수 2개 입력받아 비교하기4
a,b = input().split()
a,b = int(a), int(b)
if a != b:
    print(True)
else:
    print(False)