# 유제 4-21
# n = int(input("n: "))
# for i in range(1,2*n):
#     for j in range(1,2*n):
#         if n+2<=i+j<=3*n-2 and abs(i-j)<=n-2:
#             print(" ",end='')
#         else:
#             print("*",end='')
#     print()

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
    
def person():
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
    person()
    if lst[-1] == 31:
        print("사람 패배")
        break