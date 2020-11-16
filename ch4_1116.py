# 예제 4-8

# position = {'사원','주임','대리','과장','차장','부장','이사','상무이사','전무이사','대표이사','부사장','사장'}

# names = []
# file1 = open("이름1.txt","r", encoding = "utf8")    # encoding = "utf8" 넣어줘야 한글이름파일 열 수 있음
# while True:
#     line = file1.readline()
#     if line == '':
#         break
#     line = set(line.rstrip('\n').split())
#     names += list(line-position)               # 차집합 연산:  str과 list에서 적용 X
# names = set(names)                             # +=  :  dict, set에서 적용 X
# file1.close()

# with open("이름2.txt","w",encoding="utf8") as file2:
#     for each_name in names:
#         file2.write(each_name + " ")


# 유제 4-8
# names = ['방자','향단','월매','이몽룡','성춘향']
# with open("투표결과.txt","r",encoding="utf8") as file_n:
#     lines = file_n.read().split()          # split() 한번에 쓸 수 있네! 
# for i in names:
#     print(i, lines.count(i))
    

# 예제 4-9
# import random
# print("[보기] 가위, 바위, 보")
# example = ['가위','바위','보']
# w = "제가 이겼네요!"
# l = "제가 졌군요!"
# d = "우리 비겼네요!"

# while True:
#     user = input("당신은? ")
#     if user not in example:
#         print("[보기] 중에 입력하세요")   
#         continue
#     com = random.choice(example)
#     print("저는?", com)
#     if user == com:
#         print(d)
#     elif ((user == "가위" and com =="보") or (user == "바위" and com =="가위") or (user == "보" and com =="바위")):
#         print(l)
#     else: 
#         print(w)

# 유제 4-9
import time

n = int(input("n: "))
for i in ['3','2','1']:            # range(3,0,-1) 안됨
    print(i, end=", ")
    time.sleep(1)
print("시작!")