# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = 60
    color = 'Черный'
    name = 'Toyota'
    is_police = False

    def go(self):
        print(f'{self.color} {self.name} поехал!', end=' ')

    def stop(self):
        print(f'{self.name} остановился!', end=' ')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}!', end=' ')

    def show_speed(self):
        print(f'{self.name} едит {self.speed} км/ч!', end=' ')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость на {self.speed - 60} км/ч!', end=' ')
        else:
            print(f'{self.name} едит {self.speed} км/ч!', end=' ')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость на {self.speed - 40} км/ч!', end=' ')
        else:
            print(f'{self.name} едит {self.speed} км/ч!', end=' ')


class SportCar(Car):
    acceleration = 6.5

    def go(self):
        print(f'{self.color} {self.name} поехал с ускорением 100 км за {self.acceleration} сек.!', end=' ')

    def show_speed(self):
        print(f'{self.name} разгонится {self.speed} км/ч за {self.speed * self.acceleration / 100} cек.', end=' ')


class PoliceCar(Car):
    def speeding(self, intruder):
        if self.is_police:
            print(f'{self.name} включил сирену и начал преследование {intruder}!', end=' ')


car_1 = TownCar()
car_1.name = 'Bus'
car_1.color = 'Желтый'
car_1.speed = 80
car_1.go()
car_1.show_speed()
car_1.turn('направо')
car_1.stop()
print()

car_2 = SportCar()
car_2.name = 'Ferrari'
car_2.color = 'Красный'
car_2.acceleration = 4
car_2.speed = 120
car_2.go()
car_2.show_speed()
car_2.stop()
print()

car_3 = WorkCar()
car_3.name = 'Tractor'
car_3.speed = 30
car_3.go()
car_3.show_speed()
car_3.turn('налево')
car_3.stop()
print()

car_4 = PoliceCar()
car_4.name = 'Auto_Shrif'
car_4.go()
car_4.show_speed()
if car_3.speed > 40:
    car_4.is_police = True
    car_4.speeding(car_3.name)
if car_1.speed > 60:
    car_4.is_police = True
    car_4.speeding(car_1.name)
print()
