"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено."""

from itertools import cycle, count
for i in count(3):
    if i >10:
        break
    print(i)
c = 0
for i in cycle("ABC"):
    if c >10:
        break
    print(i)
    c+=1

list_count = [((i for i in count(3))) for _ in range(7)]
print(list_count)