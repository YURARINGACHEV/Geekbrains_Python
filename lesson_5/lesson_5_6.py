"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
import re
with open('6.txt', 'r+') as text:
    text.seek(0)
    dict_text = text.readlines()
    text.seek(0)
    d_text = text.read().split('\n')
    data_num =[]
    data_words= []
    for i in d_text:
        val = re.findall(r'[-+]?\d*\.\d+|\d+',i)
        if val !=[]:
           data_num.append(val)
    data_sum = [sum(map(int,i)) for i in data_num]
    for i in dict_text:
        data_str = [i for i in i.split()[0] if i !=':']
        data_words.append(''.join(data_str))

data_info =dict(zip(data_words,data_sum))
print(data_info)
