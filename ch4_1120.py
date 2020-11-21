# 예제 4-11
import random

people = input("사람들: ").split()
groups = int(input("그룹 숫자: "))
random.shuffle(people)
print(people)
for i in range(1,groups+1):
    print('%d조: '%i)
    for j in range(len(people)):
        print(j)
        print(j % groups+1) 
    print()

유제 4-12
year = int(input("연도: "))
if year % 400 ==0:
    print("윤년")
elif year % 100 == 0:
    print("평년")
elif year % 4 ==0:
    print("윤년") 
else:
    print("평년")

#========================================================

# 예제 4-12

while True:
    user = input("나: ")
    if "안녕" in user:
        print("컴퓨터: 만나서 반가워.") 
    elif user == "끝!":
        print("또 보자.")
        break
    else:
        print("컴퓨터: 무슨 말인지 잘 모르겠어.")
    
# 유제 4-12 (내가 푼 것) 끝말잇기 게임

# with open("후보낱말.txt","r",encoding ="euc-kr") as file2:  #대부분 인코딩 방식: utf-8, euc-kr
#     while True:
#         words = file2.readline()             # 한 줄씩 읽기
#         if words == '':                      # 빈 줄이면 멈추기
#             break
#         play = words.rstrip('\n').split()    # 한줄띄우기 떼고 띄어쓰기로 구분    
# '''문제점1: readline으로 한줄한줄 읽을 필요 없다. 
#            한 줄로 간단히 read할 수 있다 (변수 = open( ).read().split())''데

play = open("후보낱말.txt",'r',encoding = "euc-kr").read().split()
def word_game():
    com = random.choice(play) 
    print("컴퓨터: ",com)
    while True:
        user2 = input("나: ")  
        if user2.startswith(com[-1]) and len(user2) > 1:
            # if user2 not in play:               # 후보 낱말의 완성도가 높을 경우 해제 & 아래 else
            #     print("와! 내가 이겼다!")
            #     break
            try:
                pack = [i for i in play if i.startswith(user2[-1]) and len(i)>1]
                com = random.choice(pack)
                print("컴퓨터: ",com)
                continue
            except:
                print("내가 졌다. 다시 해.")
                com = random.choice(play)
                print("컴퓨터: ",com)
                continue
        else: 
            print("와! 내가 이겼다!")
            break
        
'''문제점2: user가 글자 길이가 1인 즉, 끝음절만 치면 안되는데 그런 내용 없다.
   문제점3: pack리스트 만드는데 너무 많은 줄 소모, 이차원리스트 생각하여 조건있는 리스트 한줄로 만들기'''

while True:   
    user = input("나: ") 
    if "안녕" in user:
        print("컴퓨터: 만나서 반가워.")
    elif user == "끝!":
        print("또 보자.")
        break
    elif "끝말잇기" in user:
        print("컴퓨터: 나부터 할게.")
        word_game()
    else:
        print("무슨 말인지 모르겠어")
        

# 유제 4-12(답지) 끝말잇기 게임

words = open("후보낱말.txt","r",encoding = "euc-kr").read().split()
# 이렇게 짧게 가능!

def judge(word1,word2):
    """word1은 직전 낱말, word2는 새로운 낱말"""
    # if word2 not in words:           # 후보 낱말의 완성도가 높으면 주석 해제
    #     return False
    if len(word2)==1:
        return False
    if word1[-1] == word2[0]:          # word1끝과 word2시작이 같고 길이가 2 이상이면서 word2가 words에 없는경우는 모두 True?
        return True
    else:                              # 1)word1의 끝과 Word2의 시작이 같지 않음 
        return False

def word_selection(previous_word):
    if not previous_word:             #새로 시작하는 경우
        return random.choice(words)
    else:
        available_words = [i for i in words if i[0] == previous_word[-1] and len(i) >1]
        if not available_words:       # 사용 가능한 단어가 없다면
            return ''
        else:
            return random.choice(available_words)

def word_chain():
    user_word=''
    print("컴퓨터: 나부터 할게.")
    while True:
        computer_word = word_selection(user_word)     # 찾아 고르기
        if not computer_word:
            print("컴퓨터: 내가 졌다. 다시 해.")
            user_word=''
            continue
        else:
            print(computer_word)                      #말하기
        user_word = input("나: ")
        if not judge(computer_word,user_word):
            print("컴퓨터: 와! 내가 이겼다!")
            break
while True:
    user = input("나: ")
    if user == "끝!"임
        print("컴퓨터: 또 보자.")
        break
    elif "안녕" in user:
        print("컴퓨터: 만나서 반가워.")
    elif "끝말잇기" in user:
        word_chain()
    else:
        print("컴퓨터: 무슨 말인지 잘 모르겠어")