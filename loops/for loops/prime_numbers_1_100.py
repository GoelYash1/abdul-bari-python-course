def is_prime(number):
    if number < 2:
        return False
    for j in range(2, (number // 2) + 1):
        if number % j == 0:
            return False
    return True

for i in range(1, 101):
    if is_prime(i):
        print(i)