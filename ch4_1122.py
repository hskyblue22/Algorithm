# 예제 4-18 삼각형 출력
user = int(input("n: "))
for i in range(user):
    for j in range(i+1):
        print('*', end='')
    print()

# 예제 4-18(답지)
n = int(input('n: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print('*',end='')
    print('')

# 유제 4-18 삼각형 출력
user = int(input("n: "))
for i in range(user,0,-1):
    for j in range(i):
        print('*', end='')
    print()

# ============================

# 예제 4-19 삼각형2
user = int(input("n: "))
for i in range(user,0,-1):
    for j in range(i-1):
        print(' ',end="")
    for k in range((-i)+user+1):
        print('*',end='')
    print('')

# 예제 4-19 (답지)_행렬좌표이용
n = int(input('n: '))
for i in range(1,n+1):                  # 행 좌표
    for j in range(1,n+1):              # 행좌표 고정 후 열 좌표 먼저 움직인다.
        if i+j >= n+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# 유제 4-19
num = int(input('n: '))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i <= j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#================================

# 예제 4-20
n = int(input('n: '))
for i in range(1,n+1):
    for j in range(1,2*n):
        if i+j >= n+1 and j-i <= n-1:
            print('*', end= '')
        else:
            print(' ',end='')
    print()

# 유제 4-20
n = int(input('n: '))
for i in range(1,n+1):
    for j in range(1,2*n):
        if i+j <=2*n and j-i >=0:
            print("*",end='')
        else:
            print(' ',end='')
    print()