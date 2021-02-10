# Задание № 1
def div():
    try:
        arg1 = int(input('Введите числитель '))
        arg2 = int(input('Введите знаменатель '))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка! Введите целое число'
    except ZeroDivisionError:
        return 'Ошибка! Нельзя делить на ноль'
    return res
print(div())

# Задание № 2
def my_func(name, surname, year, city, email, tel):
        print(f'Результат -  {name} {surname} {year} {city} {email} {tel}')
my_func(input('Ваше имя  '), input('Ваша фамилия '), int(input('Сколько Вам лет ')),\
        input('Ваш город '), input('Ваш email '), input('Ваш номер телефона '))

# Задание № 3
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
       return arg1 + arg2
    elif arg1 >= arg2 and arg2 <= arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(f'Результат - {my_func(int(input("Первый аргумент ")), int(input("Второй аргумент ")), int(input("Третий аргумент ")))}')

# Задание № 4
def my_func(x, y):
    return  x ** (y)
print(my_func(int(input('ведите положительное число число ')), int(input('введите целое отрицательное число '))))
def my_func(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x
print(my_func(int(input('ведите положительное число число ')), int(input('введите целое отрицательное число '))))

#Задание № 5
def summa ():
    summa_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или для выхода введите r - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'r':
                ex = True
                break
            else:
                res = res + int(number[el])
        summa_res = summa_res + res
        print(f'Сумма чисел {summa_res}')
    print(f'Финальная сумма  {summa_res}')
summa()
# Задание № 6
def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False
words = input('Введите строку из слов разделенных пробелами ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
