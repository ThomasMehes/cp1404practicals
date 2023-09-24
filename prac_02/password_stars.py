"""Program gets user password above a minimum length and returns it as *"""


def main():
    """"""
    password = get_password()
    hide_password(password)


def get_password():
    """"""
    minimum_password_length = 8
    password = input("Enter a password: ")
    while len(password) < minimum_password_length:
        print(f"password must be greater then {minimum_password_length}, try again")
        password = input("Enter a password: ")
    return password

def hide_password(password):
    """"""
    print('*' * len(password))


main()
