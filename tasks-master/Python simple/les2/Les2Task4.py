# Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть,
# состоящую ровно из k долек. Программа получает на вход три числа:
# n, m, k и должна вывести YES или NO

n = int(input('введите длину шоколадки в дольках'))
m = int(input('введите ширину шоколадки в дольках'))
k = int(input('сколько долек необходимо отломать за раз?'))

if k % n == 0:
    print('Да ломай вдоль на', int(k / n), 'долек')
elif k % m == 0:
    print('Да ломай попперек на', int(k / m), 'долек')
else:
    print('Не выйдет')
