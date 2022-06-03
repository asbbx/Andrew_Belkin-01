# 1. Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

numbers = int(input('Введите число: '))

last_number = numbers % 10
second_number = numbers % 100 // 10
third_number = numbers // 100

sum_numbers = last_number + second_number + third_number
print(f"Сумма равна = {sum_numbers}")

multiplication_numbers = last_number * second_number * third_number
print(f"Произведение чисел =  {multiplication_numbers}")
