"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.средней величины дохода сотрудников"""

with open('3.txt', 'r+') as text:
    text.seek(0)
    text_list = text.readlines()
    sum = 0
    print("Сотрудники получающие меньше 20000:")
    for i in range(len(text_list)):
        list_text = text_list[i].split()
        for j in range(len(list_text)):
            if list_text[j].isalpha()==False :
                sum+= float(list_text[j])
                if list_text[j]<"20000":
                    print(text_list[i], end='')
    print("Средняя величина дохода сотрудников равна ",sum/len(text_list))
