"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования
в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""

list_number = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 33, 33, 41]

my_new_list = [el for el in list_number if list_number.count(el) < 2]
print(my_new_list)
