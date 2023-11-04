for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(100, -1, -10):
    print(i, end=' ')
print()

number_stars = int(input("Number of Stars: "))
stars = number_stars * '*'
print(f"Number of stars {stars}")

for number_stars in range(number_stars + 1):
    # stars = number_stars * '*'
    print(f"{number_stars * '*'}")
# Maximum efficiency baby
