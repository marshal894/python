# Задание № 1
print('Добрый день')
a = 6
print(a)
b = 4
print(a + b)
name = input('ВВедите ваше имя - ')
age = int(input('Сколько Вам лет - '))
sport = input('Какой Ваш любимый вид спрота - ')
do = int(input('Сколько раз в неделю Вы занимаетесть спортом -'))
print('Ваше имя -', name, '\n Ваш возраст -', age,
      '\n Ваш любимый вид спрота -', sport, '\n В неделю -', do)

# Задание № 2
time = int(input('Введите время в секундах - '))
hour = time // 3600
minut = (time - hour * 3600) // 60
second = time - (hour * 3600 + minut * 60)
print(f'{hour:02} : {minut:02} : {second:02}')

# Задание № 3
n = int(input('Введите число n = '))
print(n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

# Задание № 4
m = abs(int(input('Введите целое положительное число - ')))
maxz = m % 10
while m >= 1:
    m = m // 10
    if m % 10 > maxz:
        maxz = m % 10
    else:
        print(maxz)
        break

# Задание № 5
vir = int(input('Введите значение прибыли - '))
izder = int(input('Введите значение издержки - '))
if vir > izder:
    ren = (vir - izder) / vir
    print(f'Фирма работает в прибыль \nРентабельность фирмы = {ren:.3f}')
    n = int(input('Введите число сотрудников '))
    prib1 = (vir - izder) / n
    print(f'Прибыль фирмы на одного сотрудника {prib1:.3f}')
if vir < izder:
    print('Фирма работает в убыток')
if vir == izder:
    print('Фирма работает в ноль')

# Задание № 6
a = int(input('Введите сколько км пробежал спортсмен за первый день - '))
b = int(input('общий результат в км нужно пробежать - '))
day = 1
rday = a
while rday < b:
    a = a + a * 0.1
    day += 1
    rday = a
print('Номер дня', day)
