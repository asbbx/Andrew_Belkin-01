x1 = float(input('Введите координаты x1 '))
y1 = float(input('Введите координаты y1 '))
x2 = float(input('Введите координаты x2 '))
y2 = float(input('Введите координаты y2 '))
if x1 != x2:
    i = (y2 - y1)/(x2 - x1)
    j = (x2*y1 - x1*y2)/(x2 - x1)
    print(f'Уравнение прямой y = {i}x + {j}')
else:
    print(f'Уравнение прямой x = {x1}')
