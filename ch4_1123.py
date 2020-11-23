# 예제 4-10 
# with open('판별대상.txt',"r",encoding='utf8') as file1:
#     while True:
#         scores = file1.readline()
#         if scores =='':
#             break
#         score = scores.rstrip('\n').split()
#         for i in range(1,4):
#             score[i] = int(score[i])
#         if score[1]+score[2]+score[3] < 10 and (score[1]+score[2]<8 or score[3]+score[2]<8):
#             print(score[0])

# (다시풀기)유제 4-10 사용자정의함수, 딕셔너리 활용_문제풀때 규칙으로 함수 지정하는거 익숙해지자

# scores ={'S':0, 'A':0,'B':0,'C':0}
# points=[2,6,4,10]
# def sum(a,b):
#     return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + a[3]*b[3]
# with open('판별대상.txt',"r",encoding='utf8') as file1:
#     while True:
#         person = file1.readline()
#         if person =='':
#             break
#         score =int(person.rstrip('\n').split())
#         result = 100 - sum(score,points)
#         if result >= 90:
#             scores['S'] += 1
#         elif result >= 80:
#             scores['A'] += 1
#         if result >= 60:
#             scores['B'] += 1
#         else:
#             scores['C'] += 1
# for key,value in result.items():
#     print(key,value)
 
# (다시풀기) 예제 4-11 : 나머지로 배분하기, for 중첩문 더 풀기
import random
# group = input("사람들: ").split()
# random.shuffle(group)
# n = int(input("그룹 숫자: "))

# for i in range(1,n+1):
#     print("%d조: "%i, end = '')
#     for j in range(len(group)):
#         if j % n == i-1:
#             print(group[j], end=' ')
#     print()
    
# 유제 4-11
# n = int(input("연도: "))
# if n % 400 == 0:
#     print("윤년")
# elif n%100 == 0:
#     print("평년")
# elif n%4 == 0:
#     print("윤년")
# else:
#     print("평년"기

# ==================================

# 예제 4-21 마름모 출력

n = int(input("n: "))
for i in range(1,2*n):
    for j in range(1,2*n):
        if n< i+j <=3*n-1 and abs(i-j)<n:
            print('*',end='')
        else:
            print(' ',end='')
    print()