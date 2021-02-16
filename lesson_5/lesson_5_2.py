"""2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""
with open('lesson_5_2.txt', 'r+') as text_les:
    num = 0
    for line in text_les:
        num += 1
        print(line, end='')
    print("\nКоличество строк первым способом = ", num)

with open('lesson_5_2.txt', 'r') as text_les_2:
    print('Количество строк вторым способом =  ', len(text_les_2.readlines()))
    count = 0
    text_les_2.seek(0)
    for _ in range(len(text_les_2.readlines())):
        text_les_2.seek(count)
        count += 1
        print("Количество слов в ", count, "строке равно ", len(text_les_2.readline().split()))

