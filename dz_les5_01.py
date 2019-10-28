# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# Функция создает папку в указанном каталоге
def new_dir(name):
	os.mkdir(name)

# Функция удаляет папку в указанном месте
def dir_rm(name):
	os.rmdir(name)

user_answer = int(input("Если нужно создать папки введите '1', если удалить '2'\n"))
if user_answer == 1:
	name = 'dir_'
	number = 1
	while number <= 9:
		new_name = name + str(number)
		if not os.path.isdir(new_name):
			new_dir(new_name)
		number += 1
elif user_answer == 2:
	name = 'dir_'
	number = 1
	while number <= 9:
		new_name = name + str(number)
		if os.path.isdir(new_name):
			dir_rm(new_name)
		number += 1
else:
	print('Неверный ввод!')
