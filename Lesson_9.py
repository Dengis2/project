#Задача №1
import time

class TrafficLight:

    __color = ["Red", "Yellow", "Green"]

    def method_running(self):
        color = self.__color
        print(f"{color[0]}")
        time.sleep(7)
        print(f"{color[1]}")
        time.sleep(2)
        print(f"{color[2]}")
        time.sleep(7)

a = TrafficLight()
a.method_running()

#Задача №2
class Road:

    def calculate(self, __length, __width):
        return (f"{(__length * __width * 25 * 5) / 1000} т.")
a = Road()
print(a.calculate(20, 5000))

#Задача №3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return f"({self.name} {self.surname})"

    def get_total_income(self):
        return f"{sum(self._income.values())}"

a = Position("Иван", "Гантелькин", "Продавец", 100, 37)
print(a.get_full_name())
print(a.get_total_income())

#Задача №4
class Car:
    def __init__(self, speed, color, name, is_police): #is_police (булево)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f"Машина {self.name} поехала"
    def stop(self):
        return f"Машина {self.name} остановилась"
    def turn(self, direction):
        return f"Машина {self.name} повернула {direction}"
    def show_speed(self):
        pass

class TownCar(Car):
    print("TownCar")
a = TownCar(69, "Grey", "Mazda", False)
print(a.go())
print(a.turn("налево"))
print(a.stop())

def show_speed(self):
    if self.speed > 60:
        print(f"Превышение скорости")
    else:
        print(f"Скорость не превышает 60")

class SportCar(Car):
    print("SportCar")
a_1 = SportCar(250, "Red", "Audi", False)
print(a_1.go())
print(a_1.turn("направо"))
print(a_1.stop())

class WorkCar(Car):
    print("WorkCar")

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости")
        else:
            print(f"Скорость не превышает 40")
a_2 = WorkCar(79, "White", "Renault", False)
print(a_2.go())
print(a_2.turn("направо"))

class PoliceCar(Car):
    print("PoliceCar")
a_3 = PoliceCar(45, "White", "Skoda", True)
print(a_3.go())
print(a_3.turn("направо"))

"""
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 ( TownCar) и 40 ( WorkCar) должно выводиться сообщение о
превышении скорости.
"""

#Задача №5
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f"Запуск отрисовки - {self.title}"
class Pen(Stationery):
    def draw(self):
        return f"Подчеркивание {self.title}"
class Pencil(Stationery):
    def draw(self):
        return f"Чертеж {self.title}"
class Handle(Stationery):
    def draw(self):
        return f"Обвести {self.title}"

stationery = Stationery("Ручка")
print(stationery.draw())
pen = Pen("Шариковая")
print(pen.draw())
pencil = Pencil("4H")
print(pencil.draw())
handle = Handle("Зеленый")
print(handle.draw())




