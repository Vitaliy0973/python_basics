''' Узнайте у пользоватеоя число n. Найдите сумму чисел n + nn + nnn.
Наприме пользователь ввел число 3. Считаем 3 + 33 + 333 = 369. '''

value = input('Введите число: ')
value_2 = value + value
value_3 = value + value + value


print(int(value) + int(value_2) + int(value_3))