# enumerate를 이용한 반복문
# f = open('선착순응모자.txt',"r",encoding = "utf8")
# names = f.read().split()
# f.close()
# in_entry = False
# for i, name in enumerate(names):
#     if name == '이성계':
#         print(i+1, '번째 응모자')
#         in_entry = True
#         break
# if not in_entry:
#     print('응모하지 않음')


# O(n^2)정렬

# 1. bubble sort(거품 정렬)
# numbers = [int(i) for i in input("숫자들: ").split()]
# for i in range(len(numbers)-1,0,-1):
#     for j in range(i):
#         if numbers[j] > numbers[j+1]:
#             numbers[j+1], numbers[j] = numbers[j],numbers[j+1]
# print(numbers)

# 2. selection sort(선택정렬)___내가 만든 것
# n = [int(i) for i in input("숫자들: ").split()]
# mini = 0
# for i in range(len(n)-1):
#     for j in range(i,len(n)-1):
#         if n[j] > n[j+1]:
#             mini = n[j+1]
#         else:
#             mini = n[j]
#     min = n.index(mini)
#     n[i],n[min] = mini, n[i]
# print(n)
''' 예전에 풀었던 알고리즘 문제에서 함수 min을 쓰지 않고 풀었던 방법이 생각나서
    기억나는 방법을 응용해서 풀었다. 
    아래 3가지 측면에서 비효율적인 것 같다. (시간복잡도가 높게 될 것 같다.)
    1) mini 를 따로 정의해주는 점
    2) 원소 값으로 비교하여 if, else 모두 사용해 mini에 값을 넣어줬다.
    3) 리스트 원소의 값으로 비교하여 mini의 인덱스(min)를 따로 정의해줘야 하는 점'''

# 2. selection sort(선택정렬)___index()사용하기
ns = [int(i) for i in input('수열: ').split()]
for i in range(0,len(ns)-1):
    min_i = ns.index(min(ns[i:]))
    # min_i = ns.index(min(ns[i:]),i)
    ns[i], ns[min_i] = ns[min_i], ns[i]
print(ns) 

# 2. selection sort(선택정렬)___답지
# nums = [int(i) for i in input('수열: ').split()]
# for i in range(len(nums)-1):
#     min_i = i                       # min_i => 리스트의 인덱스
#     for j in range(i+1,len(nums)):
#         if nums[min_i] > nums[j]:
#             min_i = j
#     nums[i], nums[min_i] = nums[min_i], nums[i]
# print(nums) 
''' 3) nums[i]를 기준으로 nums내 모든 원소를 비교하여 가장 작은 원소의 index를 저장하므로 
    인덱스를 따로 정의해 주지 않아도 된다.
    2) mini를 따로 정의하지 않고 index로 원소 값을 비교한다. 
    1) 기준 원소(nums[min_i])로 비교하므로 내가 했던 것과 달리 각각의 상황에서 최소값을
    저장해줄 필요가 없다. '''