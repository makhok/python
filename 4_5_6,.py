# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие
# для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    equ = []        # оргтехника на складе
    tr = {}         # оргтехника на выдачу

    def __init__(self):
        self.warehouse_company = []

    def receive(self):
        for el in self.equ:
            # механизм валидации на количество оргтехники
            while type(el.get('количество')) == str:
                try:
                    el.update({'количество': int(el.get('количество'))})
                except ValueError:
                    new_el = input(f'Количество {el.get("наименование")}ов {el.get("модель")} задано неверно =>'
                                   f' "количество": {el.get("количество")} => Введите числовое значение: ')
                    el.update({'количество': new_el})

            self.warehouse_company.append(el)
            print(f'На склад поступило {el.get("количество")} {el.get("наименование")}ов {el.get("модель")}')

    def transfer(self):
        for i in self.equ:
            if i.get("модель") in self.tr.keys():
                print(f'Со склада выдано в подразделение {self.tr.get(i.get("модель"))}'
                      f' {i.get("наименование")}ов {i.get("модель")}.', end='')
                # уменьшение кол-ва оргтехники на складе переданной в подразделение
                i.update({"количество": (i.get("количество") - self.tr.get(i.get("модель")))})
                print(f' Осталось => {i.get("количество")}')

    def __str__(self):
        for i in warehouse.warehouse_company:
            print(f'{i.get("наименование")} {i.get("модель")} => {i.get("количество")} шт.')
        return f'{warehouse.warehouse_company}'


class Office_equipment:
    def __init__(self, name, model, quantity, price):
        self.name = name
        self.model = model
        self.quantity = quantity
        self.price = price
        self.instance_technic = {'наименование': self.name, 'модель': self.model,
                                 'количество': self.quantity, 'цена': self.price}


class Printer(Office_equipment):
    def __init__(self, name, model, quantity, price, type_printer, print_speed):
        super().__init__(name, model, quantity, price)
        self.type_printer = type_printer
        self.print_speed = print_speed
        self.instance_technic.update({'тип принтера': self.type_printer, 'скорость печати': self.print_speed})


class Scanner(Office_equipment):
    def __init__(self, name, model, quantity, price, view_scanner, resolution_scanner):
        super().__init__(name, model, quantity, price)
        self.view_scanner = view_scanner
        self.resolution_scanner = resolution_scanner
        self.instance_technic.update({'вид сканера': self.view_scanner, 'разрешение': self.resolution_scanner})


class Xerox(Office_equipment):
    def __init__(self, name, model, quantity, price, resource_copy, price_copy):
        super().__init__(name, model, quantity, price)
        self.resource_copy = resource_copy
        self.price_copy = price_copy
        self.instance_technic.update({'ресурс': self.resource_copy, 'себистоимость копии': self.price_copy})


printer_1 = Printer('принтер', 'Brother DCP-T510W', 300, 15000, 'струйный', 15)
printer_2 = Printer('принтер', 'Canon LBP223dw', 85, 27000, 'лазерный', 33)
printer_3 = Printer('принтер', 'HP Laser 107a', 105, 20000, 'лазерный', 20)

scanner_1 = Scanner('сканер', 'Epson Perfection V19', 150, 5000, 'плашетный', '4800dpi')
scanner_2 = Scanner('сканер', 'HP ScanJet Pro N4000', 25, 7500, 'протяжный', '600dpi')
scanner_3 = Scanner('сканер', 'Plustek OpticFilm 8100', 're', 12000, 'слайд-сканер', '7200dpi')

xerox_1 = Xerox('копир', 'HP Laser MFP 135w', 110, 14219, 99, 3)
xerox_2 = Xerox('копир', 'Lexmark MX421ade', 250, 8000, 200, 5)
xerox_3 = Xerox('копир', 'Ricoh M C250FW', '210', 18000, 150, 12)

warehouse = Warehouse()
warehouse.equ = [
                 printer_1.instance_technic, printer_2.instance_technic, printer_3.instance_technic,
                 scanner_1.instance_technic, scanner_2.instance_technic, scanner_3.instance_technic,
                 xerox_1.instance_technic, xerox_2.instance_technic, xerox_3.instance_technic
                ]
warehouse.receive()
print('Всего на складе:')
print(warehouse)
print()

warehouse.tr = {'Brother DCP-T510W': 25, 'Epson Perfection V19': 10, 'HP Laser 107a': 50, 'Ricoh M C250FW': 15}
warehouse.transfer()
print('Всего на складе осталось:')
print(warehouse)
