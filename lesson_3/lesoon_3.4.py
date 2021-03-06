"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
 Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""


def mod_num(x, y):
    if y < 0:
        n = 1
        for i in range(abs(y)):
            n = n * x
        return 1 / n
    print("Ввели неправильный набор чисел")
    return mod_num(int(input('Введите  х: ')), int(input('Введите y: ')))


print(
    f"Функция mod_num = {round(mod_num(int(input('Введите  х для функции mod_num: ')), int(input('Введите y для функции mod_num: '))), 2)}")


def my_func(x, y):
    if isinstance(x, int) and y < 0:
        return 1 / (x ** abs(y))
    print("Ввели неправильный набор чисел")
    return my_func(int(input('Введите  х: ')), int(input('Введите y: ')))


print(
    f"Функция my_func {round(my_func(int(input('Введите  х для функции my_func: ')), int(input('Введите y для функции my_func: '))), 2)}")
