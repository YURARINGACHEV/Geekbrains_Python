"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""
dict_word = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result = []
with open('4.txt', 'r+', encoding='utf - 8') as text:
    text.seek(0)
    for line in text:
        print(line.split())
        if line.split()[0] in dict_word:
            word = dict_word[line.split()[0]]
            print(word)
            result.append(word + ' - ' +line.split()[2] )



with open('4.1.txt',  'w+') as translet_text:
    translet_text.seek(0)
    for i in result:
        translet_text.write(i+ '\n')





# import googletrans
#
# print(googletrans.LANGUAGES)
# from googletrans import Translator
#
# translator = Translator()
# result = translator.translate('One', dest ='en', src = 'ru')
# #
# print(result.src)
# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)
# не заработала библиотека
