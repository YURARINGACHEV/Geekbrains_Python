"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""
from sys import argv

name_script, hour, rate_per_hour, prize = argv
wage = float(hour) * float(rate_per_hour) + float(prize)

print("Заработная плата сотрудника: ", round(wage,2))
