"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json
import re

with open('7.txt', 'r+') as text_file:
    list_data = []  #список названия фирмы
    list_sum = []   # список выручки и издержек
    data_result = []    #итоговый список
    sum_val = 0     # среднее значение прибыли
    sum_data = []   # список прибыли и убытков
    dict_sum = {"average_profit": 0}    # словарь средней прибыли
    text_file.seek(0)
    d_text = text_file.read().split('\n')  # ыовд всего текста через read
    text_file.seek(0)
    list_text = text_file.readlines()  # Список всего текста
    print(list_text)
    for lines in d_text:
        val = re.findall(r'[-+]?\d*\.\d+|\d+', lines)
        if val != []:
            list_sum.append(val)

    for obj in list_sum:
        sum_val = int(obj[0]) - int(obj[1])
        sum_data.append(str(sum_val))
        data_sum = sum(map(int, [i for i in sum_data if int(i) > 0])) / len([i for i in sum_data if int(i) > 0])
    dict_sum["average_profit"] = data_sum


    for i in list_text:
        data_str = [i for i in i.split()[0]]
        list_data.append(''.join(data_str))
    dict_ifo = dict(zip(list_data, sum_data)) #список названий фирм и прибыли
    data_result.append(dict_ifo)
    data_result.append(dict_sum)
    print(data_result)
with open('7.json', 'w+') as data_json:
    json.dump(data_result, data_json)
