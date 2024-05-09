even_divisible_by_2 = [num for num in range(1, 11) if num % 2 == 0]

odd_divisible_by_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 == 0]

not_divisible_by_2_and_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]

print("Even numbers that are divisible by 2:", even_divisible_by_2)
print("Odd numbers that are divisible by 3:", odd_divisible_by_3)
print("Numbers that are not divisible by 2 and 3:", not_divisible_by_2_and_3)