# 예제 4-10
with open("판별대상.txt","r", encoding="utf8") as file2:
    while True:
        student = file2.readline()
        if student == '':
            break
        student = student.rstrip('\n').split()
        # print(student)
        for i in [1,2,3]:                            # 국어,수학,영어 이렇게 처리하네
            student[i] = int(student[i])
        con1 = student[1] +student[2]+student[3]
        con2 = student[1]+student[2]/2
        con3 = student[3]+student[2]/2
        
        if con1<10 and (con2<4 or con3<4):
            print(student[0])


# 유제 4-10
# 내가 푼 방법
# rank = ["S","A","B","C"]
# S,A,B,C = 0,0,0,0
# with open("테스트.txt","r",encoding = "utf8") as file_game:
#     while True:
#         result = file_game.readline()
#         if result == '':
#             break
#         result = result.rstrip("\n").split()
#         for i in [0,1,2,3]:
#             result[i] = int(result[i])
#         sum = 100- (result[0]*2 +result[1]*6 +result[2]*4 +result[3]*10)

#         if sum >= 90:
#             S += 1
#         elif sum >= 80:
#             A += 1
#         elif sum >= 60:
#             B += 1  
#         else:
#             C += 1
# print("S", S)
# print("A", A)
# print("B", B)
# print("C", C)

#답지
# result = {'S':0, 'A':0, 'B':0,'C':0}        # key값: str, value값: int정수

# def deduction(a,b):
#     return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]    #list[index]

# with open("테스트.txt","r",encoding ="utf8") as game:
#     while True:
#         point = game.readline()
#         if point == '':
#             break
#         point = point.rstrip('\n').split()
#         scores = [int(i) for i in point]
#         d_point = [2,6,4,10]

#         score = 100- deduction(scores,d_point)
#         if score >= 90:
#             result['S'] += 1         # result 딕셔너리에서 'S'키의 'value'값에 1더하기
#         elif score >= 80:
#             result['A'] += 1         # result 딕셔너리에서 'A'키의 'value'값에 1더하기
#         elif score >= 60:
#             result['B'] += 1         # result 딕셔너리에서 'B'키의 'value'값에 1더하기
#         else:
#             result['C'] += 1

# for key,value in result.items():
#     print(key,value)
