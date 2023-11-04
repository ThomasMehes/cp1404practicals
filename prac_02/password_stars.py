"""Program gets user password above a minimum length and returns it as *"""


def main():
    """Gets password input from user, if longer than minimum length, it is converted to *"""
    password = get_password()
    hide_password(password)


def get_password():
    """gets users input password and checks its longer than minimum length"""
    minimum_password_length = 8
    password = input("Enter a password: ")
    while len(password) < minimum_password_length:
        print(f"password must be greater then {minimum_password_length}, try again")
        password = input("Enter a password: ")
    return password

def hide_password(password):
    """converts password length into *"""
    print('*' * len(password))


main()
