''' Узнайте у пользоватеоя число n. Найдите сумму чисел n + nn + nnn.
Наприме пользователь ввел число 3. Считаем 3 + 33 + 333 = 369. '''

value = input('Введите число: ')
result = int(value) + int(value * 2) + int(value * 3)
value_2 = int(value * 2)
value_3 = int(value * 3)


print(f'{value} + {value_2} + {value_3} = {result}')