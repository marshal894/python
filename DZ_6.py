# Задание № 1
from time import sleep
class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()


# Задание № 2
class Road:
    def __init__(self, _length, _width, _massa, _thickness):
        self._length = _length
        self._width = _width
        self._massa = _massa
        self._thickness = _thickness
    def mass(self):
        return self._length * self._width * self._massa * self._thickness
m = Road(20, 5000, 25, 5)
print(m.mass())


# Задание № 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + '' + self.surname
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
        # return f'{sum(self._income.values())}'
a = Position('Иванов', ' Илья', 'Менеджер', 97000, 15000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())


# Задание № 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} начало движения'
    def stop(self):
        return f'{self.name} остановка'
    def turn_right(self):
        return f'{self.name} поворот направо'
    def turn_left(self):
        return f'{self.name} поворот налево'
    def show_speed(self):
        return f'скорость движения {self.name}  {self.speed}'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Скорость движения  {self.name}  {self.speed}')
        if self.speed >= 40:
            return f' {self.name} превышение скорости'
        else:
            return f'{self.name} Нормальная скорость'
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Скорость движения  {self.name}  {self.speed}')
        if self.speed >= 60:
            return f'  {self.name} превышение скорости'
        else:
            return f'  {self.name} Нормальная скорость'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} автомобиль полиции'
ferrari = SportCar(250, 'Red', 'ferrari', False)
opel = TownCar(35, 'White', 'opel', False)
mersedes = WorkCar(70, 'red', 'mersedes', False)
bmw = PoliceCar(90, 'Blue', 'bmw', True)
print(ferrari.show_speed())
print(opel.show_speed())
print(bmw.show_speed())
print(mersedes.show_speed())
print(mersedes.turn_left())
print(f'Сначало {opel.turn_right()}, затем {opel.stop()}')
print(f'{mersedes.go()} {mersedes.show_speed()}')
print(f'{mersedes.name} {mersedes.color}')
print(f' {ferrari.name} полицейская машина? {ferrari.is_police}')
print(f' {bmw.name}  полицейская машина? {bmw.is_police}')


# Задание № 5
class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'{self.title}. Запуск отрисовки ручкой'
class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'{self.title}. Запуск отрисовки карандашом'
class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'{self.title}. Запуск отрисовки маркером'
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())