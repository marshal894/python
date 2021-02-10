# Задание № 1
def salary():
    try:
        time = float(input('Выработка в часах - '))
        bid = int(input('Ставка в час - '))
        prize = int(input('Премия - '))
        sal = time * bid + prize
        print(f'Зарплата сотрудника {sal}')
    except ValueError:
        return print('Введите в числовом значении')
salary()

# Задание № 2
sour_list = [1, 5, 8, 10, 3, 7, 4, 3, 2, 1, 70, 7, 25]
new_list = [el for num, el in enumerate(sour_list) if sour_list[num - 1] < sour_list[num]]
print(f'Исходный список {sour_list}')
print(f'Новый список {new_list}')

# Задание № 3
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# Задание № 4
sour_list = [1, 1, 5, 4, 4, 4, 3, 7, 25, 3, 5, 55]
new_list = [el for el in sour_list if sour_list.count(el) == 1]
print(new_list)

# Задание № 5
from functools import reduce
def my_func(el_p, el):
    return el_p * el
print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Задание № 6
from itertools import count
for i in count(int(input('Введите число от 1 до 10 - '))):
    if i > 20:
        break
    else:
        print(i)

from itertools import cycle
my_list = [777, True, 5.5, 'Hello', False]
count = 0
for item in cycle(my_list):
    if count > 15:
        break
    print(item)
    count += 1

# Задание № 7
from itertools import count
from math import factorial
def fibo_gen():
    for el in count(1):
        yield factorial(el)
gen = fibo_gen()
x = 0
for i in gen:
    if x < 10:
        print(i)
        x += 1
    else:
        break