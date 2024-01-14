def greet(name, owner):
    if name == owner:
        print("Hello, boss")
    else:
        print("Hello, guest")

user_name = input("Write your name: ").lower()
greet(user_name, owner="kateryna")
# assert greet('Daniel', 'Daniel') == 'Hello, boss'
# assert greet('Greg', 'Daniel') == 'Hello, guest'