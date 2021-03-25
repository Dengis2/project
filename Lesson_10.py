#Задача №1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def __add__(self, other):
        return [[cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)] for row_1, row_2 in zip(self.matrix, other.matrix)]

matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]]) #matrix_1 = Matrix([[31, "2"], ["k", 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, 8]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_3)
print(matrix_2 + matrix_3)

#Задача №2
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def Coat(self):
        pass

    @abstractmethod
    def Suit(self):
        pass

class Cloth(Clothes):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @property
    def Coat(self):
        return self.V / 6.5 + 0.5

    @property
    def Suit(self):
        return 2 * self.H + 0.3

cloth = Cloth(5, 6)

print(f" Расход ткани на пальто {cloth.Coat}")
print(f" Расход ткани на костюм {cloth.Suit}")
print(f" Общий расход ткани {cloth.Coat + cloth.Suit}")

#Задача №3
class Cell:
    def __init__(self, cell):
        self.cell = cell
    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell - other.cell) > 0:
            return Cell(self.cell - other.cell)
        else:
            return f"Разность невозможна"
    def __mul__(self, other):
        return Cell(self.cell * other.cell)
    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, row):
        self.row = row
        return '\n'.join(['*' * row for i in range(self.cell // self.row)]) + '\n' + ('*' * (self.cell % self.row))

cell_1 = Cell(5)
cell_2 = Cell(18)
print(f"Сложение клеток - {cell_1 + cell_2}")
print(f"Разность клеток - {cell_1 - cell_2}")
print(f"Умножение клеток - {cell_1 * cell_2}")
print(f"Деление клеток - {cell_1 // cell_2}")
print(cell_2.make_order(4))