"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""

class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def calculate_weight_method(self,weight, thickness):
        calculate_weight = self._width * self._length * weight * thickness
        print("Масса асфальта, необходимого для покрытия всего дорожного полотна равна ", calculate_weight)

weitght =Road(5000, 20)
weitght.calculate_weight_method(25, 5)