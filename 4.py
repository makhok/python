# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие
# для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
from typing import Dict, Any


class Warehouse:
    equ = {}


    def __init__(self):
        self.warehouse_company = []

    def receive(self):
        self.warehouse_company.append(self.equ)
        return f'На склад поступило {self.equ.get("количество")} ' \
               f'{self.equ.get("наименование")}ов {self.equ.get("модель")}'


    #def transfer(self):
    #    return f'Со склада выдано в подразделение {self.company_division}'


class Office_equipment:
    def __init__(self, name, model, quantity, price):
        self.name = name
        self.model = model
        self.quantity = quantity
        self.price = price
        self.instance_technic = {'наименование': self.name, 'модель': self.model, 'количество': self.quantity,
                        'цена': self.price}


class Printer(Office_equipment):
    def __init__(self, name, model, quantity, price, type_printer, print_speed):
        super().__init__(name, model, quantity, price)
        self.type_printer = type_printer
        self.print_speed = print_speed

    def all_printer(self):
        return self.instance_technic.update({'тип принтера': self.type_printer, 'скорость печати': self.print_speed})



class Scanner(Office_equipment):
    pass


class Xerox(Office_equipment):
    pass


company = ('управление', 'отдел кадров', 'бухгалтерия', 'служба безопасности', 'отдел материального обеспечения')


printer_1 = Printer('принтер', 'Brother DCP-T510W', 230, 15000, 'струйный', 15)
printer_1.all_printer()
print(printer_1.instance_technic)

printer_2 = Printer('принтер', 'Canon LBP223dw', 85, 27000, 'лазерный', 33)
printer_2.all_printer()
print(printer_2.instance_technic)

printer_3 = Printer('принтер', 'HP Laser 107a', 105, 20000, 'лазерный', 20)
printer_3.all_printer()
print(printer_3.instance_technic)

warehouse = Warehouse()
warehouse.equ = printer_1.instance_technic
print(warehouse.receive())

warehouse.equ = printer_2.instance_technic
print(warehouse.receive())

warehouse.equ = printer_3.instance_technic
print(warehouse.receive())

print(warehouse.warehouse_company)
#print(warehouse.transfer())
