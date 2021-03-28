# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TrafficLight:
    __color = 'красный'

    def running(self):
        self.cl = cl
        while True:
            if self.cl == 'красный':
                print(self.cl.upper())
                self.cl = 'желтый'
                time.sleep(7)
            elif self.cl == 'желтый':
                print(self.cl.upper())
                self.cl = 'зеленый'
                time.sleep(3)
            elif self.cl == 'зеленый':
                print(self.cl.upper())
                self.cl = 'красный'
                time.sleep(10)


tr_light = TrafficLight()
cl = tr_light._TrafficLight__color
tr_light.running()
