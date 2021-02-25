"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов
на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
    проверить на практике работу декоратора @property."""
from abc import ABC, abstractmethod


class CLoth(ABC):
    @abstractmethod
    def tissue_consumtion(self):
        """подсчет расхода материала"""


class Poat(CLoth):
    """Подсчет расхода материала на пальто"""

    def __init__(self, V):
        self.t_c_p = V / 6.5 + 0.5

    def tissue_consumtion(self):
        print(f"Расход ткани на пальто {self.t_c_p:0.2f}")

    @property
    def tissue_consumption_poat(self):
        return self.t_c_p


class Costume(CLoth):
    """подсчет расхода материала на костюм"""

    def __init__(self, H):
        self.t_c_c = 2 * H + 0.3

    def tissue_consumtion(self):
        print(f"Расход ткани на костюм {self.t_c_c:0.2F}")

    @property
    def tissue_consumption_costume(self):
        return self.t_c_c


class Sum_cloth(CLoth):
    """Общий расход ткани"""

    def __init__(self, V, H):
        self.sum = Costume(H).tissue_consumption_costume + Poat(V).tissue_consumption_poat

    def tissue_consumtion(self):
        pass

    @property
    def sum_p_c(self):
        return f'Общее количество ткани {self.sum:0.2f} '

V = int(input('Введите размер пальто: '))
H = int(input('Введите размер костюма '))

poat = Poat(V)
poat.tissue_consumtion()
poat_cos = Sum_cloth(V, H)
print(poat_cos.sum_p_c)
