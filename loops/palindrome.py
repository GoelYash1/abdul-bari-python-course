number = int(input("Enter a number: "))

# Number of digits
num_of_digits = sum_of_number = reversed_num = 0

temp_num = number

while temp_num > 0:
    r = temp_num % 10
    sum_of_number += r
    num_of_digits += 1
    reversed_num = reversed_num * 10 + r
    temp_num = temp_num // 10

print(f"Digit count of the number: {num_of_digits}")
print(f"Sum of digits of the number: {sum_of_number}")
print(f"Reversed number: {reversed_num}")
print(f"Is the number palindrome? {reversed_num == number}")

