# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
our_numb_letter = int(input('Введите номер буквы: '))
our_letter = ord('a') + our_numb_letter - 1

print(f'Ваша буква - {chr(our_letter)}')
