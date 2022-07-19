# Python 기초 100제 [리스트] - 6092~6098번

#6092 - [기초-리스트] 이상한 출석 번호 부르기1
'''
첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
'''

n = int(input())
a = input().split()

for i in range(n):        # 0부터 n-1까지
    a[i] = int(a[i])      # a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장장

d = []                    # d라는 빈 리스트[] 변수를 만든다.
# 번호는 1~23 까지 있음
for i in range(24):       #[0,0,....] 이런 식으로 24개의 정수 값 0을 추가
    # d.append(값)        #d 리스트의 마지막에 원하는 값을 추가(append)해 넣음
    d.append(0)           #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n):        # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
    d[a[i]] += 1

for i in range(1, 24):    #1부터 23
    print(d[i], end=' ')

#6093 -  [기초-리스트] 이상한 출석 번호 부르기2

# (방법1)
n = int(input())
a = input().split()
d = []     # 공백 리스트 생성

for i in a:
    i = int(i)
    d.append(i) # 입력 받은 값들을 공백 리스트(d) 에 추가

d.reverse()  # 리스트 뒤집기 -> reverse()를 써서 리스트에 저장된 값들은 반대로 출력
for i in d:
    print(i, end=" ")

# (방법2)
#range(시작, 끝, 증감) #시작 수는 포함, 끝 수는 포함하지 않음. [시작, 끝)
#range(n-1, -1, -1) #n-1, n-2, ..., 3, 2, 1, 0
n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

for i in range(n-1, -1, -1):
  print(a[i], end=' ')

#6094 - [기초-리스트] 이상한 출석 번호 부르기3

#(방법1)
n = int(input())
k = input().split()

d = []  # 리스트 생성
for i in k:
    i = int(i)
    d.append(i) # 입력 받은 값들을 리스트(d)에 추가

print(min(d)) # min을 써서 리스트 d의 최소값을 출력

#(방법2)
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) : # 0부터 n-1까지의 요소를 비교하여 가장 작은 값(최소값)을 min에 넣는다
  if a[i] < min :
    min = a[i]

print(min)

#6095

#6096

#6097

#6098
