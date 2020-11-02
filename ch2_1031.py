# 2.6 조건문
# 예제 2-9
# id = input("ID: ")
# pw = input("Password: ")

# if id == "admin" and pw == "1234":
#     print("환영합니다. 관리자님!")
# print("어서 오십시오")   

# 유제 2-9
# serial_numbers= [1111555,2223322,2521249,8504037]
# user_num = int(input("일련번호를 입력하세요(일곱자리)"))
# if user_num in serial_numbers:
#     print("정상")
# else:
#     print("비정상")



# 2.7 반복문

# 예제 2-13
# n = int(input("몇 단? "))
# for i in range(1,10):
#     print(n,"X",i,"=",n*i)

# n = int(input("몇 단? "))
# i = 1
# while i <10:
#     print(n,"X",i,"=",n*i)
#     i += 1

# 유제 2-13
# num = int(input("몇부터?: "))       # 사용자로부터 받은 원시코드 변형되므로 권장X
# while num>=0:
#     print(num)
#     num -=1

# num = int(input("몇부터?: "))
# for i in range(num,-1,-1):          # range(n,-1,-1)!
#     print(i)


# 예제 2-14
# many = int(input("몇 개? "))
# n_list = []
# for i in range(1,many+1):
#     num = input(f"숫자 {i}:")
#     n_list += [num]                   # [num] -> 11이 11로 들어감 / num -> ['1','1', ...]

# for j in range(many-1,-1,-1):
#     print(n_list[j])


# 유제 2-14
# many = int(input("몇 개? "))
# sum = 0
# for i in range(1,many+1):
#     num = int(input(f"숫자{i}: "))
#     sum += num

# aver = sum / many
# print(aver)


# 2.9 함수
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# 유제 2-21
# def reverse():
#     rev = ""
#     n = int(input("몇 글자 이름입니까? "))
#     name = input("이름: ")
#     for i in range(-1,(n*(-1))-1,-1):
#         word = name[i]
#         rev += word
#     print(rev)

# reverse()
                                                                     