"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
 с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""
my_list = [7, 5, 3, 3, 2]
print('Для выхода нажмите q')
while True:
    print(sorted(my_list, reverse=True))
    n = input("Введите новый элемент рейтинга: ")
    if n == 'q':
        break
    elif n.isdigit():
        my_list.append(int(n))
        print(sorted(my_list, reverse=True))
        my_list.remove(int(n))
    else:
        print('Введите число: ')
