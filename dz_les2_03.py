''' Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, 
осень). Напишите решения через list и через dict '''

month = int(input('Введите номер месяца: '))

method = int(input('Если решаем через list жми 1, если через dict жми 2: '))

if method == 1:
	if month < 1 or month > 12:
	    print('Вы ввели неверный номер месяца.')
	else:
		# Решение через list		
		season_list = [
		    None, 'winter', 'winter', 'winter', 'spring', 'spring', 
		    'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 
		    'autumn'
		    ]
		print(f'Ваш месяц относиться к времени года: {season_list[month]}.')
elif method == 2:
	if month < 1 or month > 12:
	    print('Вы ввели неверный номер месяца.')
	else:
		# Решение через dict
		season_dict = {
			1 : 'winter', 2 : 'winter', 3 : 'winter',
			4 : 'spring', 5 : 'spring', 6 : 'spring',
			7 : 'summer', 8 : 'summer', 9 : 'summer',
			10 : 'autumn', 11 : 'autumn', 12: 'autumn'
			}
		print(f'Ваш месяц относиться к времени года: {season_dict[month]}.')
elif method < 1 or method > 2:
	print('Вы ввели неверный номер.')
