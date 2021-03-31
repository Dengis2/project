#Задача №1
class Data:
    def __init__(self, data):
        self.data = data
    @classmethod
    def f_1(cls, data):
        d, m, y = map(int, data.split('-'))
        return d, m, y

    @staticmethod
    def f_2(obj):
        d, m, y = obj
        if 0 < d < 32 and 0 < m < 13 and 2020 < y < 2022:
            return True
        else:
            return f"Вы указали значение дней - {d}, необходимо указать значение дней от 1 до 31 \nВы указали значение месяцев - {m}, необходимо указать значение месяцев от 1 до 12 \nВы указали значение лет - {y}, необходимо указать значение дней от 2020 до 2022"

one = Data.f_1("28-03-2021")
print(one)
print(Data.f_2(one))

#Задача №2
a = input("Введите число: ")
b = input("Введите число: ")
class OwnError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    try:
        print(a / b)
    except:
        print("Деление на ноль недопустимо")

#Задача №3
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
rices = []
while True:
    try:
        rices.append(int(input("Введите число: ")))
    except ValueError:
        print("Вы ввели не число")
        continue
    else:
        print(f"Вы ввели числа {rices}")

#Задача №4,5,6
class Stock:

    def __init__(self):
        self.dict = {}

    def add_equipment(self, equipment, quantity):
        equipment_type = equipment.__class__.__name__
        try:
            self.dict[equipment_type][equipment.name] += quantity
        except KeyError:
            if equipment_type not in self.dict:
                self.dict[equipment_type] = {}
                self.dict[equipment_type][equipment.name] = quantity
            elif equipment.name not in self.dict[equipment_type]:
                self.dict[equipment_type][equipment.name] = quantity

    def del_from_stock_to(self, equipment):
        for self.equipment in self.dict.keys():
            if True:
                del self.dict[self.equipment]
                return

class OfficeEquipment:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.name} {self.year}"

class Printer(OfficeEquipment):
    def __init__(self, name, year, color):
        super().__init__(name, year)
        self.color = color

    def __str__(self):
        return f"{self.name} {self.year} {self.color}"

    def action(self):
        return f"Печатает"

class Scanner(OfficeEquipment):
    def __init__(self, name, year, type_scanner):
        super().__init__(name, year)
        self.type_scanner = type_scanner

    def __str__(self):
        return f"{self.name} {self.year} {self.type_scanner}"

    def action(self):
        return f"Сканирует"

class Xerox(OfficeEquipment):
    def __init__(self, name, year, format_xerox):
        super().__init__(name, year)
        self.format_xerox = format_xerox

    def __str__(self):
        return f"{self.name} {self.year} {self.format_xerox}"

    def action(self):
        return f"Копирует"


stock = Stock()
printer = Printer('HP', 2021, 'Цветной')
stock.add_equipment(printer, 4)
printer = Printer('BP', 2020, 'Черно-белый')
stock.add_equipment(printer, 10)
scanner = Scanner('Samsung', 2020, 'Multifunction')
stock.add_equipment(scanner, 7)
scanner = Scanner('BP', 2021, 'Null')
stock.add_equipment(scanner, 8)
xerox = Xerox('LG', 2019, 'Multifunction')
stock.add_equipment(xerox, 5)
print(stock.dict)
stock.del_from_stock_to(printer)
print(stock.dict)

#Задача №7
class ComplexNumb:
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"{self.a}"
    def __add__(self, other):
        return ComplexNumb(self.a + other.a)
    def __mul__(self, other):
        return ComplexNumb(self.a * other.a)

Numb_1 = ComplexNumb(complex(1, 2))
Numb_2 = ComplexNumb(complex(3, 4))
print(f"Сложение чисел - {Numb_1 + Numb_2}")
print(f"Умножение чисел - {Numb_1 * Numb_2}")
