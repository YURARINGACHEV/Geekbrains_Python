"""6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text."""

lower_letters = [chr(i) for i in range(97, 123)]
upper_letters = [chr(i) for i in range(65, 91)]


def int_func(str_text):
    """Преобразование первой буквы слова из прописной в заглавную"""

    str_text = list(str_text)
    text = ''
    flag = True
    if len(str_text) == 1:
        print(upper_letters[lower_letters.index(str_text[0])])
    else:
        for i in range(1, len(str_text)):
            while flag:
                if str_text[0] == lower_letters[lower_letters.index(str_text[0])]:
                    text = text + upper_letters[lower_letters.index(str_text[0])]
                    flag = False
            text = text + str_text[i]
    print(text)

int_func(input("Введите слово с прописной буквы: "))

