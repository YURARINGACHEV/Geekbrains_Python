"""Для списка реализовать обмен значений соседних элементов, т.е.
 Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
  При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""
list_elem = []
print("Заполните список произвольными элементами. Для остановки заполнения нажмите 'q' ")
n = 0
while True:
    n +=1
    el = input(f'Введите элемент №{n}: ')
    if el == 'q':
        break
    list_elem.append(el)
print(list_elem)
for i in range(0,(len(list_elem)-1),2):
    list_elem[i], list_elem[i+1]=list_elem[i+1], list_elem[i]
print(list_elem)

# my_list = list(input('Заполните список элементов'))
# print(my_list)
# for i in range(0,(len(my_list)-1),2):
#     my_list[i], my_list[i+1]=my_list[i+1], my_list[i]
# print(my_list)