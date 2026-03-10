while True:
    password = input("Enter your password: ")

    has_let = any(char.isalpha() for char in password)
    has_num = any(char.isdigit() for char in password)

    if has_let and has_num:
        print("Password accepted.")
        break
    else:
        print("Invalid password, try again.")