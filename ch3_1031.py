# 3.2.1
# a= []
# count = 0
# for i in range(5):
#     a.append([])
# print(a)
#     for _ in range(5):
#         count += 1
#         a[i].append(count)
# print(a)
        
# for문 에서 index 필요없을 때 _ 사용
# for _ in range(5):
#     print("weekend!")


# 유제 3-1, 예제 3-2
# suit = ['♠', '♣', '♡', '◇']
# denomination = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# for i in suit:
#     for j in denomination:
#         print(i+j)

# print([i+j for i in suit for j in denomination])



# 3.2.2
# a ="가나다라마바사아"
# b ="abcdefghijklmnop"

# # change = [a,b]       너무 길어!
# # a = change[1]
# # b = change[0]

# change = a
# a = b
# b = change
# print(a)
# print(b)


# 유제 3-2 : tuple사용하지 않고 객체 값 서로 교환하기

# a = 1
# b = 2
# c = 3

# change = a
# a = b
# b = c
# c = change
# print(a,b,c)


# 유제 3-3
def name_division(name):
    return name[0], name[1:]
성, 이름 = name_division("박진달래")
print(성)
print(이름)