# Ch4
# 예제 4-1: 여러 개의 정수를 입력받아 그 중 가장 큰 숫자를 출력하는 프로그램
numbers = input("여러 개의 숫자 입력: ")
numbers = [int(i) for i in numbers.split()]
print("최대값: ",max(numbers))

#============================================
numbers = input("여러 개의 숫자 입력: ")
numbers = [int(i) for i in numbers.split()]
max_number = numbers[0]
for i in numbers:
    if i > max_number:
        max_number = i
print("가장 큰 숫자:",max_number)


# 유제 4-1: 여러 개의 정수를 입력받아 그 중 가장 작은 숫자를 출력하는 프로그램
num = input("여러 개의 숫자 입력: ")
num = num.split()
number = []
for i in num:
    number += [int(i)]
min_number = number[-1]
for i in number:
    if i < min_number:
        min_number = i
print("가장 작은 숫자:", min_number)
    

# 예제 4-2: 정수묶음, 한개의 정력(x)를 따로 입력받아 정수묶음안에 x가 몇 개 있는지 출력
numbers = input("정수 묶음: ").split()
# numbers = [int(i) for i in numbers.split()] --> 정수로 계산하는 문제x -> int로 형변환 필요x
x = input("찾을 정수: ")                        # 정수로 계산x -> int로 형변환 필요x

count = 0
for i in numbers:
    if x == i:
        count += 1
print("포함: ",count)

#======================================
numbers = input("정수 묶음: ").split()
x = input("찾을 정수: ")
print("포함: ",numbers.count(x))


# 유제 4-2
numbers = input("정수 묶음: ").split()
x = input("찾을 정수: ")
if x in numbers:
    print("인덱스: ",numbers.index(x))
else:
    raise ValueError

#======================================
numbers = input("정수 묶음: ").split()
x = input("찾을 정수: ")
idx = -1
for i in range(len(numbers)):     # 정수묶음 길이를 통해 인덱스 구하기
    if numbers[i] == x:
        idx = i
        break
if idx == -1:
    raise ValueError
else:
    print("인덱스: ",idx)


# 예제 4-3
user = input("문자열: ")
end = ""
for i in range(len(user)-1,-1,-1):
    end += user[i]
print("거꾸로: ",end)

#============================
string = input("문자열: ")
for i in range(len(string)-1,-1,-1):
    print(string[i],end='')           # 거꾸로 출력하면 되는 문제이므로 변수를 뒤집을 필요는 없다


# 예제 4-3: 문자열 완전히 반대로 출력, 재귀함수 사용
def f(m):
    if m == 0:
        return ""
    a = user[m-1]+str(f(m-1))
    return a
user = input("문자열: ")    
print(f(len(user)))

#==========================
def reverse(i):
    if i == -1:
        return
    print(string[i],end='')
    reverse(i-1)

string = input("문자열: ")
reverse(len(string)-1)

#===========================
print(string[::-1])