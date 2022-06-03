# 5. Пользователь вводит две буквы.
# Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.

first_character = ord(input('Введите начало диапазона: '))
second_character = ord(input('Введите конец диапазона: '))
first_position = first_character - ord('a') + 1
second_position = second_character - ord('a') + 1
between_characters = second_character - first_character - 1

print(f'Позиция первой буквы {first_position}, '
      f'позиция второй буквы {second_position}, '
      f'кол-во букв между ними - {between_characters}')
