"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TOD0: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# 4. Loop that neatly prints
max_length = max(len(state) for state in CODE_TO_NAME)
for state_code in CODE_TO_NAME:
    print(f"{state_code:3} is {CODE_TO_NAME[state_code]:{max_length}}")

state_code = input("Enter short state: ").upper()  # 3. Allows lowercase inputs to work
while state_code != "":
    try:  # 5. exceptions for EAFP
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

