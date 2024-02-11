user_string = 'Andromeda, M 31, NGC 224'
letters = ""
digits = ""
for i in range(len(user_string)):
    if user_string[i].isdigit():
        digits += user_string[i]
    elif user_string[i].isalpha():
        letters += user_string[i]

print(len(letters))
print(len(digits))
