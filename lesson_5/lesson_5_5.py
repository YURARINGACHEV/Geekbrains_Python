"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
from random import randint

with open('text_5.txt', 'w+') as text_num:
    for i in range(10):
        text_num.write(str(randint(0, 100)) + ' ')
    text_num.seek(0)
    text_sum = text_num.readline().split()
    s = 0
    sum = sum(map(int, text_sum))
    print(sum)
