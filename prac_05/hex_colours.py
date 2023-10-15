"""
CP1404 Practical
Program allows user to look up hexadecimal colour codes
"""

HEX_COLOUR_CODES = {"Chocolate": "#d2691e", "BubbleGum": "#ffc1cc", "Burgundy": "#800020", "Crystal": "#a7d8de",
                    "BabyBlue": "#89cff0", "Daffodil": "#ffff31", "AbsoluteZero": "#0048ba"}

# Create a mapping of lowercase color names to the original mixed-case names
color_name_mapping = {name.lower(): name for name in HEX_COLOUR_CODES}
# Needed this so it could handle both mixed-case inputs without making my Keys be only upper or lower case

# Show user the list of options:
max_length = max(len(colour) for colour in HEX_COLOUR_CODES)
for colour in HEX_COLOUR_CODES:
    print(f"{colour:{max_length}} is {HEX_COLOUR_CODES[colour]:8}")

colour = input("Enter a colour: ").lower()  # Allows input inputs to work
while colour != "":
    try:
        original_case_name = color_name_mapping[colour]
        print(original_case_name, "is", HEX_COLOUR_CODES[original_case_name])
    except KeyError:
        print("Invalid colour choice")
    colour = input("Enter a colour: ").lower()
