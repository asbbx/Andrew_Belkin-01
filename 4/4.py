# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
from random import randint, uniform

date_type = input(
    "Введите первую букву типа данных integer, float, characters: ")
start_range = input("Введите начальное значение диапазона: ")
end_range = input("Введите конечное значение диапазона: ")

if date_type == 'i':
    result = randint(int(start_range), int(end_range))
if date_type == 'f':
    result = uniform(float(start_range), float(end_range))
if date_type == 'c':
    result = chr(randint(ord(start_range), ord(end_range)))

print(result)
