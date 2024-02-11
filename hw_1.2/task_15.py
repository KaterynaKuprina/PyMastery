user_input = input("Write your string: ")
if user_input.isalpha():
    print("In your string only letters")
elif user_input.isdigit():
    print("In your string only digit")
else:
    print("Wrong string")