"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
  Реализовать вывод данных о пользователе одной строкой."""
def data_base(name, sername, year_of_birdth, city, email, phone_num):
        print(f"Мое имя {name}, Фамилия {sername}, родился в {year_of_birdth} году. Живу в городе {city}. Email {email}, телефон {phone_num}")


data_base(name = input("Введите имя: "), sername = input('фамилия: '), year_of_birdth = input("год рождения: "),
          city = input('город проживания'), email = input('email'), phone_num = input('телефон'))