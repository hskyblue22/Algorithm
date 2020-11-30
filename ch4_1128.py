# 유제 4-21
n = int(input("n: "))
for i in range(1,2*n):
    for j in range(1,2*n):
        if n+2<=i+j<=3*n-2 and abs(i-j)<=n-2:
            print(" ",end='')
        else:
            print("*",end='')
    print()


# 유제 4-22 내 답안
import random

def com2(n,r):
    global lst
    for _ in range(r):
        print(n, end= ' ')
        lst += [n]
        if n == 31:
            break
        else:
            n += 1
    print()

def com1():
    global lst
    print('컴퓨터: ',end='')
    r= random.randint(1,3)
    if len(lst) == 0:
        com2(1,r)
    else:
        com2(lst[-1]+1,r)
    
def people():
    global lst
    print("사람: ", end = '')
    numbers = input().split()
    for i in numbers:
        lst += [int(i)]
        if i == 31:
            break

lst = []
while True:
    com1()
    if lst[-1] == 31:
        print("컴퓨터 패배")
        break
    people()
    if lst[-1] == 31:
        print("사람 패배")
        break


# 다시 풀기
def com(previous_n):
    com_answer = [i for i in range(previous_n+1, previous_n+random.randint(1,3)+1) if i<32]
    print('컴퓨터: ',end='')
    for j in com_answer:
        print(j, end= ' ')
        if j == 31:
            break
    print()
    return com_answer

def game():
    nums = []
    while True:
        if len(nums) == 0:
            nums = com(0)
        else:
            person_num = person()             # 문제에서 사람은 규칙을 준수한다고 가정했음
            if lose("사람",person_num):
                break
            com_nums = com(person_num)
            if lose("컴퓨터",com_nums[-1]):
                break
    
def person():
    list_numbers = [int(i) for i in input("사람: ").split()]
    for j in list_numbers:
        if j == 31:
            break
    return list_numbers[-1]

def lose(who,n):
    if n == 31:
        print(who,"패배")
        return True                  # game()에서 n == 31이면 if True => break 되어서 while문 끝난다.
    # else:                            return True없으면 사람: 으로 입력하도록 나옴
    #     return False               # return False없어도 성립됨!

game()

# 예제 4-22 답지
def judge(name,n):
    '''참여자의 승패를 판단하는 함수'''
    if n==31:
        print(name,'패배')
        return True
    else:
        return False

def br31():
    '''참여자의 턴 및 게임의 진행 전반을 관리하는 함수'''
    user_numbers = [0]
    while True:
        computer_numbers = computer_turn(user_numbers)
        if judge('컴퓨터',computer_numbers[-1]):
            break
        user_numbers = user_turn()
        if judge('사람',user_numbers[-1]):
            break

def computer_turn(previous_numbers):
    '''컴퓨터의 턴에 숫자를 결정하고 출력하는 함수'''
    last_number = random.randint(previous_numbers[-1]+1,previous_numbers[-1]+3)
    if last_number >= 31:
        last_number = 31
    numbers = [i for i in range(previous_numbers[-1]+1,last_number+1)]
    # 숫자 결정 완료

    print('컴퓨터: ',end='')
    for i in numbers:
        print(i,end=' ')
    print()
    # 숫자 출력 완료

    return numbers

def user_turn():
    '''사용자 턴에 숫자를 입력받아서 이를 처리하는 함수'''
    numbers = [int(i) for i in input("사람: ").split()]
    return numbers   

if __name__ =="__main__":
    br31()                                  

