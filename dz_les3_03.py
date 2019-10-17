''' Реализовать функцию my_func(), которая принимает три
позиционных аргумента, и возвращает сумму наибольших двух
аргументов. '''

def my_func(var1, var2, var3):

    ''' Вычесляем сумму 2-х наибольших аргументов'''

    args = (var1, var2, var3)
    var1 = max(args)
    var2 = 0
    for i in args:
        if i > var2 and i != var1:
            var2 = i
    return var1 + var2

print(my_func(100, 200, 30))
