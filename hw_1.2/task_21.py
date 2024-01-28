user_string = input("Write your string: ")

for i in range(len(user_string)):
    print(f'{i} - {ord(user_string[i])}')