# Задание № 1
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:3}", end="")

    def __str__(self,):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[-1, 10, 1],
            [-15, 5, 4],
            [7, 3, -11]])

new_m = Matrix([[-2, 5, 7],
                [15, 0, 5],
                [3, 5, -2]])

print(m.__add__(new_m))


# Задание № 2
class Clothes:

    def __init__(self, param):
        self.param = param

    @property
    def get_sq_full(self):
        return str(f'Для пошива пальто и костюма нужно: {(self.param / 6.5 + 0.5) + (self.param * 2 + 0.3):.2f}')


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        pass


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(1)
costume = Costume(1)
print(coat.consumption())
print(costume.consumption())
print(coat.get_sq_full)


# Задание № 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return  self.quantity + other.quantity

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return  sub  if sub > 0 else 'Операция вычитания невозможна '

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity



    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(28)
cell1 = Cell(2)
print(cell + cell1)
print(cell - cell1)
print(cell * cell1)
print(cell / cell1)
print(cell.make_order(8))