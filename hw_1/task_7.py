user_input = input("Write your string: ")

new_string = " "
for i in range(len(user_input)):
    if i % 3 != 0:
        new_string = new_string + user_input[i]

print(new_string)
