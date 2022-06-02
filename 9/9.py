# 9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

f_number = int(input('Введите 1 число: '))
s_number = int(input('Введите 2 число: '))
t_number = int(input('Введите 3 число: '))

if s_number < f_number < t_number or t_number < f_number < s_number:
    print(f'Средним числом является - {f_number}')
elif f_number < s_number < t_number or t_number < s_number < f_number:
    print(f'Средним числом является - {s_number} ')
else:
    print(f'Средним числом является - {t_number}')
