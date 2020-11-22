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


# 예제 4-8 복습
# position= {'사원','주임','대리','과장','차장','부장','이사','상무이사','전무이사','대표이사','부사장','사장'}
# mix = []
# with open("이름1.txt","r", encoding="utf8") as file_n:  # file내용 읽어오기
#     while True:
#         lines = file_n.readline()
#         if lines == '':
#             break
#         mix += lines.rstrip('\n').split()
#     name = set(mix) - position
# with open('이름3.txt',"w",encoding='utf8') as file2:    # file내용 쓰기
#     for each_name in name:
#         file2.write(each_name+' ')

'''1) with open( ) as filename: ==> ':' 잊지 말고 써주기
   2) set(집합)에서는 중복된 요소 삭제된다.
   3) set(집합): +/- 가능[합집합, 차집합] , list: +/- 불가능
   4) file.write(내용): ( )안 write내용 적어줘야 함
   5) file.write는 print()와 달리 자동줄바꿈 안된다. '''

# 예제 4-8
with open("투표결과.txt","r",encoding='utf8') as file3:
    names = file3.read().split()
for name in set(names):
    print(name, names.count(name))

'''1) set(names): 투표결과에 중복된 이름을 제거하므로 따로 인기투표에 참여한
                  이한 리스트를 만들 필요 없다! '''