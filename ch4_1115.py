# 예제 4-1

# numbers = input("여러 개의 숫자 입력: ")
# numbers = [int(i) for i in numbers.split()]
# # print("가장 큰 숫자: ",max(numbers))

# max_number = numbers[0]
# for i in numbers:
#     if i > max_number:
#         max_number = i
# print("가장 큰 숫자: ",max_number)


# 예제 4-2

# nums = input("정수 묶음: ").split()        # 리스트 형식으로 출력됨
# find = input("찾을 정수: ")
# count = 0
# for i in nums:
#     if i == find:
#         count += 1
# print("포함:",count)
# print("포함:",nums.count(find))           # 리스트의 메서드 count()를 통해서

# 유제 4-2
# numbers = input("정수 묶음: ").split()
# num = input("찾을 정수: ")
# if num in numbers:
#     print("인덱스:",numbers.index(num))
# else:
    # raise ValueError

# idx = -1
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         idx = i
#         break
# if idx == -1:
#     raise ValueError
# else:
#     print("인덱스:",idx)


# 예제 4-3

# word = input("문자열: ")
# for i in range(len(word)-1,-1,-1):
#     print(word[i],end="")

# 유제 4-3

# def f(n):
#     if n == -1:
#         return
#     print(string[n],end="")
#     f(n-1)
# string = input("문자열: ")
# f(len(string)-1)

# def f(n):
#     if n == -1:
#         return ""
#     return user[n] + str(f(n-1))
    
# user = input("문자열: ")
# print(f(len(user)-1))


# 예제 4-6

# 출력: 달팽이 배열
# 입력: 정사각 달팽이 배열의 가로/세로 길이
# direction: 방향 -> d로 표현

# def main():
#     n = int(input("n: "))
#     snail = [[0 for j in range(n)] for i in range(n)]      # n =3일때 [[0,0,0,],[0,0,0],[0,0,0]]
#     i, j = 0, -1            # 반복문 첫 작동시 (0, 0)에서 시작되도록 설정
#     value = 1
#     i_d, j_d = 0, +1    # 시작은 우측방향 진행
#     while value <= n**2:
#         i += i_d      # 진행
#         j += j_d
#         if i == n or j == n or snail[i][j] != 0:  # snail[4][-1] = snail[4][4] i,j가 i_d,j_d에 의해 값이 변해서 아직 값이 들어가지 않은 상태여야하지만
#             #-1이 들어가면 방금 생성된 값을 지정하므로 != 0 하다.
#             i -= i_d  # 진행 취소
#             j -= j_d
#             i_d, j_d = d(i_d, j_d)      # 방향 전환
#         else:
#             snail[i][j] = value
#             value += 1
#     print_snail(snail, n)

# def d(i_d, j_d):   # 시계방향으로 진행 방향이 바뀌도록 조절
#     if i_d == 0 and j_d == +1: return (+1, 0)           # 우->하
#     elif i_d == +1 and j_d == 0: return (0, -1)         # 하->좌
#     elif i_d == 0 and j_d == -1: return (-1, 0)         # 좌->상
#     elif i_d == -1 and j_d == 0: return (0, +1)         # 상->우

# def print_snail(snail, n):
#     for i in range(n):
#         for j in range(n): print("%4d" % snail[i][j], end='')
#         print()

# if __name__ == "__main__":
#     main()

def sna():
    n = int(input("n: "))
    snail = [[0 for j in range(n)] for i in range(n)]      # j 가 먼저 변함
    value = 1
    i,j = 0, n-1
    s = +1
    k = n-1
    for f in range(n):               # 첫번째 행 채우기(좌->우  n번)
        snail[0][f] = value
        value += 1

    while k > 0:
        for _ in range(k):
            i = i+s
            snail[i][j] =value
            value += 1
        for _ in range(k):
            j = j-s
            snail[i][j] = value
            value += 1
        k -= 1
        s = s*(-1)

    print_snail(snail,n)

def print_snail(snail,n):
    for i in range(n):
        for j in range(n):
            print("%4d" %snail[i][j], end ="")
        print()

sna()