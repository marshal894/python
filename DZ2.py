# Задание № 1
list = [1, 1.5, 'Привет', 5, True]
count = 0
while count < len(list):
      print(type(list[count]), list[count])
      count += 1

# Задание № 2
count = int(input('Введите количество чисел в списке - '))
list = []
a = 0
b = 0
while a < count:
    list.append(int(input('Введите числ - ')))
    a +=1
for coun in range(int(len(list)/2)):
   list[b], list[b + 1] = list[b + 1], list[b]
   b += 2
print(list)

# Задание № 3
mons = int(input('Введите номер месяца - '))
list = ['зима', 'весна', 'лето', 'осень']
if mons == 12 or mons == 1 or mons == 2:
     print(list[0])
elif mons == 3 or mons == 4 or mons == 5:
     print(list[1])
elif mons == 6 or mons == 7 or mons == 8:
     print(list[2])
elif mons == 9 or mons == 10 or mons == 11:
     print(list[3])
else:
     print('Такого месяца нет')
mons = int(input('Введите номер месяца - '))
dict = {1 : 'зима', 2 : 'весна' , 3 : 'лето', 4 : 'осень'}
if mons == 12 or mons == 1 or mons == 2:
    print(dict.get(1))
elif mons == 3 or mons == 4 or mons == 5:
     print(dict.get(2))
elif mons == 6 or mons == 7 or mons == 8:
    print(dict.get(3))
elif mons == 9 or mons == 10 or mons == 11:
    print(dict.get(4))
else:
    print('Такого месяца нет')

# Задание № 4
stroh = input('Введите строку из нескольких слов, разделенных пробелами:\n' )
list = [ ]
nom = 1
for el in range(stroh.count(' ') + 1):
    list = stroh.split()
    if len(str(list)) <= 10:
         print(f'{nom} {list [el]}')
         nom += 1
    else:
         print(f'{nom} {list [el] [0:10]}')
         nom += 1

# Задание № 5
list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {list}')
print('число 0 - выход')
digit = int(input("Введите число "))
while digit != 0:
     for el in range(len(list)):
         if list[el] == digit:
             list.insert(el + 1, digit)
             break
         elif list[0] < digit:
             list.insert(0, digit)
         elif list[-1] > digit:
             list.append(digit)
         elif list[el] > digit and list[el + 1] < digit:
             list.insert(el + 1, digit)
     print(f"текущий список - {list}")
     digit = int(input("Введите число "))

#Задание № 6
qwol = int(input('Введите количество товара '))
n = 1
my_dict = []
list = []
analys = {}
while n <= qwol:
    my_dict = dict({'название': input('введите название '), 'цена': input('Введите цену '),
                    'количество': input('Введите количество '), 'eд': input('Введите единицу измерения')})
    list.append((n, my_dict))
    n += 1
    analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(list)
print(analys)
