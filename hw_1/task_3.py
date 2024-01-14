user_input = input("Write your string: ")

half_string = len(user_input) // 2
half1, half2 = user_input[:half_string], user_input[half_string:]

print(half2 + half1)