from collections import Counter

inventory = Counter(apple = 50,mango=100,banana=120, orange = 70)
order = Counter(apple = 10,banana=12, orange = 5)

def update_inventory(order):
    inventory.subtract(order)

update_inventory(order)
print(inventory)