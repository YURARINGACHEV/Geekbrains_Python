""" Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операцин."""

temp = int(input("Введите число: "))
max_num = 0
while temp > 0:
    i = temp % 10
    temp = temp // 10
    if max_num <= i:
        max_num = i
print("Самая большая цифра в числе = ", max_num)