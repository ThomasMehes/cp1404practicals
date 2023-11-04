

total_cost = 0
counter = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invaild number of items!")
    number_of_items = int(input("Number of items: "))
while number_of_items > counter:  # negative to stop
    price_of_item = float(input("Price of item: "))
    total_cost = total_cost + price_of_item
    counter += 1
print(f"Total price for {number_of_items} is ${total_cost:.2f}")