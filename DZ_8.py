# Задание № 1
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('28 - 2 - 2021')
print(today)
print(Data.valid(1, 1, 2045))
print(Data.valid(1, 15, 2020))
print(Data.valid(35, 11, 2020))
print(Data.extract('12 - 12 - 2020'))
print(today.extract('15 - 1 - 2021'))
print(Data.valid(28, 2, 2021))


# Задание № 2
class Division:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_null(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f"На ноль делить нельзя!!!")


numerator = float(input("Введите числитель "))
denominator = float(input("Введите знаменатель "))
print(Division.divide_by_null(numerator, denominator))



# Задание № 3
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):


        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')

            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())



# Задание № 4
class Sklad:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price} {self.quantity}'


class Printer(Sklad):
    def __init__(self, series, name, price, quantity):
        super().__init__(name, price, quantity)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.price} {self.quantity}'

    def action(self):
        return 'Печатает'


class Scanner(Sklad):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def action(self):
        return 'Сканирует'


class Xerox(Sklad):
    def __init__(self, name, price, quantity):
        super().__init__(name, price,quantity)

    def action(self):
        return 'Копирует'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5)
unit_3 = Xerox('Xerox', 1500, 1)
print(unit_1.action())
print(unit_2.action())
print(unit_3.action())


# Задание № 5
class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price} {self.quantity}'


class Printer(Equipment):
    def __init__(self, series, name, price, quantity):
        super().__init__(name, price, quantity)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.price} {self.quantity}'

    def action(self):
        return 'Печатает'


class Scanner(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price,quantity)

    def action(self):
        return 'Копирует'



sklad = Sklad()
# создаем объект и добавляем
scanner = Scanner('hp', 321, 90)
sklad.add_to(scanner)
scanner = Scanner('hp', 311, 97)
sklad.add_to(scanner)
scanner = Scanner('hp', 330, 99)
sklad.add_to(scanner)
printer = Printer('e-320','sony', 126, 2018)
sklad.add_to(printer)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('Scanner')
print()
print(sklad._dict)



# Задание № 6
class Sclad:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):

        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Sclad.reception(self)


class Printer(Sclad):
    def to_print(self):
        return f'печатает {self.numb} '


class Scanner(Sclad):
    def to_scan(self):
        return f'сканирует {self.numb} '


class Xerox(Sclad):
    def to_copier(self):
        return f'копирует  {self.numb} '

unit1 = Printer('hp', 2000, 5, 10)
unit2 = Scanner('Canon', 1200, 5, 10)
unit3 = Xerox('Canon', 1500, 1, 15)
print(unit1.reception())
print(unit2.reception())
print(unit3.reception())



# Задание № 7

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(5, -1)
z_2 = ComplexNumber(7, 5)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)



