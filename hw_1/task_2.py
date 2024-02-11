user_input = input(" Write your string: ")

our_string = user_input.strip(" ")
new_our_string = our_string.count(" ") + 1

print(new_our_string)