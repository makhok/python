# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class Complex_number:
    def __init__(self, val, im):
        self.val = val  # действительная часть числа
        self.im = im    # мнимая часть числа
        self.comp = complex(self.val, self.im)  # комплексное число

    def __add__(self, other):
        return f'{self.comp} + {other.comp} = ' \
               f'{Complex_number(self.val + other.val, self.im + other.im)}'

    def __mul__(self, other):
        return f'{self.comp} * {other.comp} = ' \
               f'{Complex_number(self.val * other.val - self.im * other.im, self.val * other.im + self.im * other.val)}'

    def __str__(self):
        return f'{complex(self.val, self.im)}'


complex_1 = Complex_number(1, 2)
complex_2 = Complex_number(3, 4)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
