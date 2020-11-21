# 예제 4-13

# n = int(input("자연수: "))         
# if int(n**0.5) != n**0.5:              # 거듭제곱(**)
#     print("자연수인 양ㄱ의 제곱근이 존재하지 않음")
# else:
#     print("양의 제곱근")

# 유제 4-13

# n = int(input('숫자: '))
# if n % 2 ==0:
#     print("짝수")
# else:
#     print("홀수")

#====================================

# 예제 4-14
from math import factorial as fa

# n = int(input('n: '))
# r = int(input('r: '))
# print(fa(n)//fa(n-r))

# 유제 4-14

# n = int(input('n: '))
# r = int(input('r: '))
# print(fa(n)// (fa(r)*fa(n-r)) )
#====================================

# 예제 4-15 약수구하기

# n = int(input('n: '))
# a = [i for i in range(1,n+1) if n % i ==0] 
# for i in a:
#     print(i, end =' ')


# 유제 4-15 소수구하기(내 답)

# num = int(input('n: '))
# only = [i for i in range(1,num+1) if num % i ==0]
# if len(only) == 2:
#     print("소수")
# else:
#     print("소수 아님")

# # 유제 4-15 소수구하기(답지)
# n = int(input("n: "))
# prime_number = True                     # 먼저 prime_number변수 True로 지정
# for i in range(2,int(n**0.5)+1):
#     if n % i ==0:
#         prime_number = False            # 나머지 0인 수(나눠지는 수) => False
#         break
# if prime_number:                        # prime_number = True : for문에서 나눠진 것 없음
#     print("소수")
# else:
#     print("소수 아님")

#================================

# 예제 4-16 최대공약수
# a = int(input('a: '))
# b = int(input('b: '))
# num_a = [i for i in range(1,a+1) if a % i ==0]
# num_b = [i for i in range(1,b+1) if b % i ==0]
# common = [i for i in num_a if i in num_b]
# print(max(common))

# 최대공약수 함수
# import math
# print(math.gcd(a,b))

# 다른 풀이(답지)
# a = int(input('a: '))
# b = int(input('b: '))
# if a>b:                       # a가 b보다 작게하기
#     a,b=b,a
# a_numbers = []
# for i in range(1, int(a**0.5)+1):
#     if a % i ==0:
#         a_numbers.append(i)
#         a_numbers.append(a//i)
# common_divisor=[]
# for i in a_numbers:
#     if b % i==0:
#         common_divisor.append(i)
# print(max(common_divisor))


# 유제 4-16 최소공배수
# a = int(input('a: '))
# b = int(input('b: '))

# if a < b:                        # a가 b보다 크게하기
#     a,b = b,a
# common_mul = [a*i for i in range(1,b+1) if a*i % b ==0]
# print(common_mul[0])

# 다른방법(거의 비슷해)
# for i in range(1,b+1):
#     if a*i % b ==0:
#         print(a*i)
#         break

#===================================

# 예제 4-17 완전제곱수
# k = int(input('k: '))
# n = int(k**0.5)
# i = 2*n-1
# print('n: ',n,'\ni: ',i)

# 유제 4-17 월일숫자
def plus(lst,ad1,ad2):
    lst.append(str(ad1)+str(ad2))
m_day = []
for i in range(1,13):
    if i == 2:
        for j in range(1,28):
            plus(m_day,i,j)
    elif i in [4,6,9,11]:
        for j in range(1,30):
            plus(m_day,i,j)
    else:
        for j in range(1,31):
            plus(m_day,i,j)

m_day = [int(i) for i in m_day]
i for i in range(1,)