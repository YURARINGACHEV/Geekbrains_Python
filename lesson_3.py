""" Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
 пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.ран."""
n = int(input("Введите число n: "))
nn = str(n) +str(n)
print("nn = " ,nn)
nnn = str(n) +str(n) + str(n)
print("nnn = " ,nnn)
sum = n + int(nn) + int(nnn)
print("sum = ", sum)