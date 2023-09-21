

user_name = input("Enter name: ")
print(f"(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>>")
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {user_name}")
    elif choice == 'G':
        print(f"Goodbye {user_name}")
    else:
        print("Invalid input, must be Capital H, G or Q")
    print(f"(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>>")
print("Finished")
