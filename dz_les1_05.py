''' Спортсмен занимается ежедневными пробежками. В первый день его 
результат составил a километров. Каждый день спортсмен увеличивал 
результат на 10% относительно предыдущего. Требуется определить 
номер дня, на который общий результат спортсмена составить не 
менее b километров. Программа должна принимать значения параметров 
a и b и выводить одно натуральное число - номер дня. '''

distance = int(input('Введите растояние (км) которое пробежал спортсмен в первый день: '))
full_distance = int(input('Введите общее растояние (км), которое необходимо пробежать: '))
day = 1
sum_distance = 0
sum_distance +=  distance

while sum_distance < full_distance:
	distance += distance / 100 * 10
	sum_distance += distance
	day +=1

print(f'Номер дня, в который спортсмен достигнет неообходимой дистанции : {day}')


