"""3. Реализовать функцию my_func(), которая
принимает три позиционных аргумента, и возвращает
сумму наибольших двух аргументов."""


def my_func(num_1, num_2, num_3):
    if num_1 >= num_2 and num_3 >= num_2:
        num = num_1 + num_3
        return num
    elif num_2 >= num_1 and num_3 >= num_1:
        num = num_2 + num_3
        return num
    else:
        num = num_1 + num_2
        return num


print(my_func(3, 4, 5))
