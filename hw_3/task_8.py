my_list = [3, 12, 67, 24, 97, 45, 44, 121]
n = 50
bigger_list = []
for num in my_list:
    if num > n:
        bigger_list.append(num)

print(bigger_list)