# Python 기초 100제 [종합] - 6077~6091번

#6077 - 짝수 합 구하기
n = int(input())

# sum : 짝수의 합
sum = 0


for i in range(1, n+1):
    if i%2 == 0:
        sum += i

print(sum)

#6078 - 원하는 문자가 입력될 때까지 반복 출력하기
while True:
    a = input()
    print(a)
    if a != 'q':
        continue
    else:
        break

#6079 - 언제까지 더해야 할까?
a = int(input())
sum = 0

for i in range(1, a+1):
    sum += i
    if sum>=a:
        print(i)
        break

#6080 - 주사위 2개 던지기
n,m = input().split()

n,m = int(n), int(m)

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i,j)

#6081 - 16진수 구구단 출력하기
a = input()
n = int(a,16)
for i in range(1,16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#6082 - 3 6 9 게임의 왕이 되자
n = int(input())

# 1부터 n까지
for i in range(1, n + 1):
    # %는 나눈 값의 몫이 나온다. i가 10보다 작을 때는 나누기가 안되서 나머지값인 i가 그대로 나온다.

    if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):
        print("X", end=' ')
    else:
        print(i, end=' ')

#6083 - 빛 섞어 색 만들기
r,g,b = input().split()
r,g,b = int(r), int(g), int(b)

n = 0

for i in range (r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            n += 1
print(n)

#6084 - 소리 파일 저장용량 계산하기
h,b,c,s = map(int,input().split())

# 공식
cal = (h*b*c*s) / (8*1024*1024)

#문제에 나온 조건
#h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.
if h <= 48000 and b <= 32 and b%8 == 0 and c <= 5 and s <=6000:
    # 출력 조건
    # 단, 소수점 첫째 자리까지의 정확도로 출력하고 MB를 공백을 두고 출력한다.
    print(format(cal, ".1f"),'MB')

#6085 - 그림 파일 저장용량 계산하기
w,h,b = map(int,input().split())

# 공식
cal = (w*h*b) / (8*1024*1024)

# 제한
# 단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.
# 단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
if 1<= w <=1024 and 1<= h <= 1024 and 1<= b <= 40 and b%4 == 0:
    print(format(cal, '.2f'), 'MB')

#6086 - 거기까지! 이제 그만~
a = int(input()) #사용자 입력값
s = 0
c = 0
# s는 전체 합(누적) / c는 1씩 커지는 값
while True:
    s += c
    c += 1

    if s>= a:
        break
print(s)

#6087 - 3의 배수는 통과
n = int(input())

for i in range(1, n+1): # 1부터 사용자가 입력한 값까지
    if i % 3 == 0:
        continue # 다음 반복 단계로 넘어간다. -> 위의(if문)조건이 맞을 때
    print(i, end=' ')

#6088 - 수 나열하기1

# 등차 수열
a,d,n = input().split()
a,d,n = int(a), int(d), int(n) # 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)  -> 사용자한테 입력 받음

print(a + (n-1) * d)

'''
위 대신 하단 for문도 사용 가능
s=a
for i in range(2, n+1):
   s+=d

print(s)
'''
#6089 - 수 나열하기2

# 등비 수열
a,r,n = input().split() # 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)
a,r,n = int(a), int(r), int(n)

print(a * r ** (n-1))

#6090 - 수 나열하기3
'''
예를 들어
1 -1 3 -5 11 -21 43 ... 은
1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.
'''

a,m,d,n = input().split() # 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)
a,m,d,n = int(a), int(m), int(d), int(n)

for i in range(2, n+1):
    a = a * m + d
print(a)

#6091 - 함께 문제 푸는 날

a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

d = 1
# 입력 받은 3개의 수로 나눴을 때 각각 나머지가 0일 때 값이 곧 최소 공배수
while d%a != 0 or d%b != 0 or d%c != 0:
    d += 1
print(d)
