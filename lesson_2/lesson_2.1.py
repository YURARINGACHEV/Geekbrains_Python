"""Создать список и заполнить его элементами различных типов данных.
 Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

my_list = [1, '123', 'Hi', (1,2,3), {'sad','ad', 'hf'}, {1:'a',2:'b'} ]
for i in range(len(my_list)):
    print(type(my_list[i]))