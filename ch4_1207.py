# quick sort(퀵정렬)__방법1

# def main():
#     numbers = [int(i) for i in input("수열: ").split()]
#     quick_sort(numbers)
#     print(numbers)

# def quick_sort(numbers):
#     quick(numbers, 0, len(numbers)-1)

# def quick(numbers, start, end):
#     if end-start <= 0:
#         return
#     pivot_i = start      # pivot_i : 기준값의 인덱스
#     for i in range(start+1, end+1):
#         if numbers[i] < numbers[pivot_i]:
#             numbers.insert(pivot_i, numbers.pop(i))
#             pivot_i += 1
#     quick(numbers, start, pivot_i -1)
#     quick(numbers, pivot_i+1, end)

# main()

# quick sort(퀵정렬)__방법2

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [n for n in array[1:] if n <= pivot]
        bigger = [n for n in array[1:] if n > pivot]
        return quickSort(less) + [pivot] + quickSort(bigger)

numbers = [35, 60, 40, 45, 55, 20, 100, 70, 85]
result = quickSort(numbers)
print(result)