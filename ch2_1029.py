# 예제 2-16

not_mine = ["용인시","둔산동","번동","장안구","온천동","구로구","군포시"]
address_list = []

while True:
    address = input("주소: ")
    check = False
    for i in not_mine:
        # print(check)
        if i in address:
            check = True          
        # if check:                # 반복문의 시작부분으로 올라간 후 for문의 변수를 진행한다.
        #     continue             
        ''' input->address="용인시"-> i="용인시" -> check=True -> continue -> i="둔산동" -> i in address? -> i="번동"->,,,-> +[address]
            input->address="번동"-> i="용인시"-> if조건 해당 x, 다시 반복문 시작으로-> i="둔산동"->if조건해당x->i="번동"->check=True->,,,->+[address]
            if check문이 for문안에 있는 경우 ==> for문 다 돌고 아래 명령어 실행하므로 not_mine에 있는 글자라해도 아래 명령어실행으로 []에 추가됨'''

    if check==True:                # (if check==True) 또는 (if check:)   / check=True로 하면 오류 남 
        continue
    
    address_list = address_list + [address]
    print(address_list)



# 예제 2-16 

answer = []
for i in range(1,100):       # 100보다 작으면서 놓치지 말기
    if i % 2 != 0:
        if i % 3 != 0:
            if i % 7 ==0 :
                answer = answer + [i]

print(answer)


#==========================

for i in range(1,100):
    if i % 2==0 or i % 3 ==0 or i % 7 !=0:
        continue
    else:
        print(i)             # 리스트로 나타내라는 말 문제에 없으니 이렇게도 가능하다!


    