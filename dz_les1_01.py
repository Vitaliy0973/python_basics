''' Пользователь вводит время в секундах. Переведите время в часы, 
минуты и секунды и выведите в формате чч:мм:сс. Используйте 
форматирование строк. '''

def two_number(x):
	if len(x) < 2:
		x = f'0{x}'
	return x

user_time = int(input('Введите время в секундах: '))
if user_time < 3600:
	hour = '00'

	minuts = two_number(str(user_time // 60))

	secondes = two_number(str(user_time % 60))

	print(f'Время: {hour}:{minuts}:{secondes}')

elif user_time >= 3600:
	hour = two_number(str(user_time // 3600))

	minuts = two_number(str(user_time % 3600 // 60))

	secondes = two_number(str(user_time % 3600 % 60))

	print(f'Время: {hour}:{minuts}:{secondes}')