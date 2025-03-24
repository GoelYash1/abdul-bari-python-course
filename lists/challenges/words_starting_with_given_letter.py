food = input("Enter food items space separated: ").split()
start_letter = input("Enter a char: ").upper()

ans_list = []

for item in food:
    if item.upper().startswith(start_letter):
        ans_list.append(item)

print(ans_list)