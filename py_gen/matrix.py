
def sum_diagonal_elems(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


def print_matrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

def print_matrix_2(matrix,n,m):
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=" ")
        print()

def create_matrix(n,m):
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = input()
    return matrix

def create_square_matrix_from_string(size):
    matrix = []
    for i in range(size):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix

# На вход программе подаются два натуральных числа n и  m, каждое на отдельной строке — количество строк и столбцов
# в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; п
# одряд идут элементы сначала первой строки, затем второй, и т.д.
#
# Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.
#
# Формат входных данных
# На вход программе подаются два числа  n и m — количество строк и столбцов в матрице, далее идут
# n×m слов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.

def create_and_print_matrix():
    n = int(input())
    m = int(input())
    mtx = create_matrix(n,m)
    print_matrix(mtx,n,m)
    print()
    print_matrix_2(mtx, n, m)


def create_square_matrix_and_sum_diagonal_elems():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    print(sum_diagonal_elems(mtx))

# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести n чисел — для каждой строки количество элементов матрицы,
# больших среднего арифметического элементов данной строки.
def avg_value_in_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum / len(list)


def more_than_avg():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    for i in range(len(mtx)):
        avg = avg_value_in_list(mtx[i])
        counter = 0
        for j in range(len(mtx)):
            if mtx[i][j] > avg:
                counter += 1
        print(counter)

def max_below_main_diagonal():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    max = mtx[0][0]
    for i in range(n):
        for j in range(0,i+1):
            if max < mtx[i][j]:
                max = mtx[i][j]
    print(max)
