"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали')

    def stop(self):
        print('Стоп')

    def turn(self):
        pass

    def show_speed(self):
        print(f'Текущая скорость автомобиля = {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Вы привысили скорость")
        else:
            print(f'Текущая скорость автомобиля = {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Вы привысили скорость")
        else:
            print(f'Текущая скорость автомобиля = {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police == 1:
            print('Полиция')


work_car = WorkCar(int(input('Введите скорость: ')), input('Введите цвет: '), input('Введите имя: '), is_police=input("Введите ноль или один "))
work_car.show_speed()

town_car = TownCar(int(input('Введите скорость: ')), input('Введите цвет: '), input('Введите имя: '), is_police=input("Введите ноль или один "))
town_car.show_speed()

sport_car = SportCar(int(input('Введите скорость: ')), input('Введите цвет: '), input('Введите имя: '), is_police=input("Введите ноль или один "))
sport_car.show_speed()

police_car = PoliceCar(int(input('Введите скорость: ')), input('Введите цвет: '), input('Введите имя: '), is_police=input("Введите ноль или один "))
police_car.show_speed()