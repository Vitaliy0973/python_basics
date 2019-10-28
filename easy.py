import os

# Функция создает папку в указанном каталоге
def new_dir(name):
	os.mkdir(name)

# Функция удаляет папку в указанном месте
def dir_rm(name):
	os.rmdir(name)
	