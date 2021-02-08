"""Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
 Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
 но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func()."""

lower_letters = [chr(i) for i in range(97, 123)]
upper_letters = [chr(i) for i in range(65, 91)]


def int_func(str_text):
    """Преобразование первой буквы слова из прописной в заглавную в списке слов"""

    str_text = str_text.split()
    list_str = []
    for str_list in str_text:
        text = ''
        flag = True
        str_list = list(str_list)
        if len(str_list) == 1:
            list_str.append(upper_letters[lower_letters.index(str_list[0])])
        else:
            for i in range(1, len(str_list)):
                while flag:
                    if str_list[0] in lower_letters:
                        text = text + upper_letters[lower_letters.index(str_list[0])]
                        flag = False
                text = text + str_list[i]
            list_str.append(text)
    print(" ".join(list_str))


int_func(input("Введите слова через пробел с прописной латинской буквы: "))
