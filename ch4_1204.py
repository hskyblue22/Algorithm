# insertion sort(삽입 정렬)__내가 푼 것

numbers = [int(i) for i in input('숫자들: ').split()]
for i in range(1, len(numbers)):
    j = i-1
    while (j >= 0 and numbers[i] < numbers[j]):
        j -= 1
    put = numbers.pop(i)
    numbers.insert(j+1,put)          
print(numbers)

# insertion sort(삽입 정렬)__답지

# n = [int(i) for i in input('수열: ').split()]
# for i in range(1, len(n)):
#     for j in range(i-1,-1,-1):
#         if n[j] > n[j+1]:
#             n[j], n[j+1] = n[j+1], n[j]
#         else:
#             break
# print(n)