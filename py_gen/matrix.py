
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

create_square_matrix_and_sum_diagonal_elems()