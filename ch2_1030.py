# 2.8 제어문 심화
# 유제 2-17 
while True:
    user = input("몇 단? ")
    if user=="x":
        break
    else:
        user = int(user)
        for i in range(1,10):
            print(user,"X",i,"=",user*i)
# 예제 2-17
for i in range(1,10):
    for x in range(1,10):
        for y in range(1,10):
            print(i,"X",y,"X",x,"=",i*y*x)


# 2.10 클래스               
# 예제 2-22
sentence = input("입력: ")
sentence = sentence.replace(',','')
sentence = sentence.replace('.','')
sentence = sentence.replace("'",'')
sentence = sentence.replace(' ','')
print(sentence)
# 유제 2-22
def make_title():
    new_title = ""
    title = input("영화 제목: ")
    sp = title.split()
    for i in sp:
        word = i.capitalize()
        new_title += word + " "
    print(new_title)
       
make_title()

# ========================

def make_title2(title):
    title = title.split()
    new_title = ''
    for each_word in title:          # 각 단어안에서 순서로 쪼개서 붙여서 나타낼 수도 있군
        new_title += each_word[0].upper + each_word[1:].lower() + ''
    return new_title[:-1]            # new_title의 마지막에 붙은 공백은 떼어낸 문자열 반환
                                     # 뒤에  ''공백을 이렇게 return을 이용해서 떼는 방법도 있다!
make_title2()

# 예제 2-23
list_for_user = []
while True:
    print()
    print(list_for_user)
    print("1: 추가, 2: 삽입, 3: 수정, 4: 삭제, 5: 종료")
    user = int(input("무엇을 할 겁니까? : "))
    if user == 5:
        break
    elif user == 1:
        add = input("추가할 값: ")
        list_for_user.append(add)
    elif user == 2:
        add = input("삽입할 값: ")
        order = input("몇 번째로 삽입? ")
        list_for_user.insert(int(order)-1, add)
    elif user == 3:
        delete = int(input("몇 번째 값 수정? "))
        modified_one = input("수정값: ")
        list_for_user.remove(list_for_user[delete-1])
        list_for_user.insert(delete-1,modified_one)
    elif user ==4:
        delete = input("삭제할 값: ")
        list_for_user.remove(delete)
    else:
        print("올바른 값을 입력해주세요.")
        continue
    
# 유제 2-23
list_number = []                       # numbers_list = list(range(1,46))
for i in range(1,46):                  # 나는 3줄로 적었는데 이렇게 한 줄로 적을 수도 있음!
    list_number += [i]
pop = input("빼려고 하는 공은? ")
list_number.remove(int(pop))
print(list_number)


# 예제 2-26
from random import shuffle
n_list = list(range(1,46))
shuffle(n_list)
print(n_list[:6])

# 유제 2-26
from random import choice
from winsound import Beep
from time import sleep
n_list = list(range(1,46))
winning_numbers = []

for i in range(6):
    print(f"{i}번째 숫자를 추첨합니다!")
    sleep(2)
    lucky = choice(n_list)
    n_list.remove(lucky)              # 중복 방지
    winning_numbers.append(lucky)
    Beep(1320,500)
    print(winning_numbers[i])
    print("")

print("보너스 번호를 추첨합니다!")
sleep(2)
lucky = choice(n_list)
n_list.remove(lucky) 
winning_numbers.append(lucky)
Beep(1320,500)
print(winning_numbers[6])
print("")
print("당첨번호는 "+str(winning_numbers[:6])+"입니다.")
print("보너스 번호는 "+str(winning_numbers[6])+"입니다.")


