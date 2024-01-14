user_input = input("Word with many hhhhh:  ").lower()

our_string = user_input[:user_input.find("h")] + user_input[user_input.rfind("h") + 1:]

print(our_string)

