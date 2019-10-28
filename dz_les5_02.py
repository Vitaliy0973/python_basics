# Напишите скрипт, отображающий папки текущей директории.

import os

# Создаем список содержимого дериктории
content = os.listdir()

# Вывод списка всех папков в дериктории
print([i for i in content if os.path.isdir(i)])