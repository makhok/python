# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три
# дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов методы должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.

class Stationery:
    title = 'Наименование'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


my_pen = Pen()
my_pen.title = 'КАРАНДАШ'
my_pen.draw()

my_pencil = Pencil()
my_pencil.title = 'РУЧКА'
my_pencil.draw()

my_handle = Handle()
my_handle.title = 'МАРКЕР'
my_handle.draw()
