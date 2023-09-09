my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
items_greater_then_10 = []

# parts 1 and 2 of exercise
for item in my_list:
    if item >= 10:
        print(item)
        items_greater_then_10.append(item)

print(items_greater_then_10)

# part 3
number_to_compare = input("Please enter a number to compare against the list \n")
compared_items = []
for item in my_list:
    if item >= int(number_to_compare):
        compared_items.append(item)

print(compared_items)