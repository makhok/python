# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.Примеры матриц вы найдете в методичке.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.

# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_list = str(self.matrix)
        return matrix_list.replace("[", "").replace(",", "").replace("] ", "\n").replace("]]", "\n")

    def __add__(self, other):
        self.sum_matrix = []
        for i in range(len(self.matrix)):
            sum_list = []
            for j in range(len(self.matrix[i])):
                sum_list.append(self.matrix[i][j] + other.matrix[i][j])
            self.sum_matrix.append(sum_list)
        return Matrix(self.sum_matrix)


matrix_1 = Matrix([[31, 22, 37], [43, 51, 86]])
print(matrix_1.matrix)
print(matrix_1)

matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, 8]])
print(matrix_2.matrix)
print(matrix_2)

matrix_3 = Matrix([[3, 5, 8], [8, 3, 7]])
print(matrix_3.matrix)
print(matrix_3)

print(f'{matrix_1.matrix} + {matrix_3.matrix} = {(matrix_1 + matrix_3).matrix}')
print(matrix_1 + matrix_3)
