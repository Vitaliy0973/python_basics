# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import os

name = input('Введите название файла, который необходимо скопировать: ')
path = os.getcwd() + '/' + name[:-3] + '_copy' + name[-3:]
print(path)
shutil.copyfile(name, path)
