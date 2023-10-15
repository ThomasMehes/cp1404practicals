"""
Email processor
Estimate: 45 minutes
Actual: 70 minutes
"""


def main():
    """program stores users' emails and names in a dictionary
    and continues to ask the user for their email until they enter a blank one."""
    email_storage = {}
    email = input("Enter your Email: ")

    while email != "":
        username = strip_email_address(email)
        username = username.split(".")
        name = extract_name(username).title()

        is_name_correct = input(f"Is {name} your name? (Y/N) ").upper()
        if is_name_correct == "Y":
            correct_name = name
        else:
            correct_name = input("Enter your name: ")

        email_storage[correct_name] = email

        email = input("Enter your Email: ")

    for name, email in email_storage.items():
        print(f"{name} ({email})")


def strip_email_address(input_string):
    """Removes all characters after @ which is the email address"""
    index = input_string.find("@")
    if index != -1:
        return input_string[:index]
    else:
        return input_string


def extract_name(username_parts):
    """Removes all unwanted characters so the name is the only thing preserved"""
    characters_to_remove = ".,!?'*$#1234567890"
    name = " ".join(username_parts)
    name = "".join(char for char in name if char not in characters_to_remove)
    return name


main()
