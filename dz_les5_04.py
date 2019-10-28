# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import shutil
import easy

print('Вас приветствует консольная утилита для работы с файлами.')
while True:
	print('Меню:')
	print(' [1] - перейти в папку')
	print(' [2] - посмотреть содержимое текущей папки')
	print(' [3] - удалить папку')
	print(' [4] - создать папку')
	print('Для завершения программы введите "q".')
	do = input('Введите номер действия: ')
	if do == 'q':
		break
	try:
		if int(do) == 1:
			print('Вы находитесь в: ', os.getcwd())
			while True:
				do_dir = input('Введите адрес по которому необходимо перейти или "q", что бы вернуться назад: ')
				if do_dir == 'q':
					break
				try:
					os.chdir(do_dir)
				except FileNotFoundError as e:
					print('Вы ввели неверный адрес дериктории.')
					continue
				print('Вы успешно перешли в дерикторию: ', os.getcwd())
				break
		elif int(do) == 2:
			content = os.listdir()
			print(f'Содержимое текущей дериктории: {content}')
		elif int(do) == 3:
			while True:
				file_name = input('Какую папку удалить? Чтобы вернуться назад введите"q". ')
				if file_name == 'q':
					break
				try:
					easy.dir_rm(file_name) # Используем подключенный модуль easy.py
				except FileNotFoundError as e:
					print('Такой папки не существует.')
					continue
				print(f'Папка {file_name} была удалена')
				break
		elif int(do) == 4:
			while True:
				file_name_two = input('Введите имя для новой папки. Чтобы вернуться назад введите"q". ')
				if file_name_two == 'q':
					break
				try:
					easy.new_dir(file_name_two) # Используем подключенный модуль easy.py
				except PermissionError as e:
					print('Вы ввели недопустимый символ в названии файла.')
					continue
				print(f'Папка {file_name_two} успешно создана.')
				break
	except ValueError as e:
		print('Не верный ввод.')
		continue
