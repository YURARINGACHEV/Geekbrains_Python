"""Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)"""

class Warker():

    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_full_name(self):
        print(f"Имя сотрудника {self.name} {self.surname}")
        print(self._income)

class Position(Warker):

    def __init__(self,name, surname, position, **income ):
        super().__init__(name,surname,position,**income)

    def get_full_name(self):
        print(f"Имя сотрудника {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход сотрудника {self._income['wage']} у.е. плюс бонус {self._income['bonus']} у.е.")
warker = Position('Jon', 'Smit', 'inginer', wage= 1000, bonus=100)
warker.get_full_name()
warker.get_total_income()