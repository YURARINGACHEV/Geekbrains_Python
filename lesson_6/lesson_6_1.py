"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет
7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт."""
import turtle
import time

turtle.speed(0)
pen = turtle.Pen()


class TrafficLight():
    def __init__(self, *color):
        self.__color = color

    def running(self):
        num = 0
        while num < 2:
            num += 1
            colors = ['red', 'yellow', 'green']
            count = 0
            x = 0
            y = 100
            if len(self.__color) != 3:
                return print('нарушена работа режимов.')
            for col in colors:
                if self.__color[count] == col:
                    TrafficLight._red_circle(self, self.__color[count], x, y)
                    print(f'Запуск {self.__color[count]}')
                    if count == 1:
                        time.sleep(2)
                    else:
                        time.sleep(7)
                    TrafficLight._red_circle(self, 'black', x, y)
                    count += 1
                    y -= 100
                else:
                    return print('нарушена работа режимов.')

    def _red_circle(self, red, x, y):
        pen.color(red)
        pen.begin_fill()
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.circle(50)
        pen.end_fill()


traf = TrafficLight('red', 'yellow', 'green')
traf.running()
turtle.done()


# import turtle
# import time
#
# turtle.speed(10)
# pen = turtle.Pen()
#
#
# class TrafficLight():
#     def __init__(self, *color):
#         self.__color = color
#
#     def running(self):
#
#         if len(self.__color) != 3:
#             return print('нарушена работа режимов.')
#         red, yellow, green = self.__color
#         if red == 'red':
#             TrafficLight._red_circle(self, red)
#             print(f'Запуск {red}')
#             time.sleep(7)
#         else:
#             return print('нарушена работа режимов.')
#         if yellow == 'yellow':
#
#             TrafficLight._yellow_circle(self, yellow)
#             print(f'Запуск {yellow}')
#             time.sleep(2)
#         else:
#             return print('нарушена работа режимов.')
#
#         if green == 'green':
#             TrafficLight._green_circle(self, green)
#             print(f'Запуск {green}')
#             time.sleep(7)
#         else:
#             return print('нарушена работа режимов.')
#
#     def _red_circle(self, red):
#         pen.color(red)
#         pen.begin_fill()
#         pen.up()
#         pen.goto(0, 100)
#         pen.down()
#         pen.circle(50)
#         pen.end_fill()
#
#     def _yellow_circle(self, yellow):
#         pen.begin_fill()
#         pen.color(yellow)
#         pen.up()
#         pen.goto(0, 0)
#         pen.down()
#         pen.circle(50)
#         pen.end_fill()
#
#     def _green_circle(self, green):
#         pen.begin_fill()
#         pen.color(green)
#         pen.up()
#         pen.goto(0, -100)
#         pen.down()
#         pen.circle(50)
#         pen.end_fill()
#
#
# traf = TrafficLight('red', 'yellow', 'green')
# traf.running()
# turtle.done()
