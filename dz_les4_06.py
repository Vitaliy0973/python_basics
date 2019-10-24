''' Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. '''

from itertools import (
	count,
	cycle
	)
from random import randint

# бесконечный итератор, генерирующий целые числа, начиная с указанного
start = int(input('С какого числа начать генерацию чисел? '))
for i in count(start):
	print(i)

# Создаем список из 10 рандомных чисел в пределах от 1 до 10
the_list = []
i = 0
while i < 11:
	the_list.append(randint(1, 20))
	i += 1
print(the_list)

# бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее
for i in cycle(the_list):
	print(i)
