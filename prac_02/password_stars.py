
minimum_password_length = 8
password = input("Enter a password: ")
while len(password) < minimum_password_length:
    print(f"password must be greater then {minimum_password_length}, try again")
    password = input("Enter a password: ")
print('*' * len(password))
