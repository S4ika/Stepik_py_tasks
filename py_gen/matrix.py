
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

def max_in_area():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    max = mtx[0][0]
    for i in range(n):
        for j in range(0, n):
            if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j) or (i == j) or (i + j + 1 == n):
                if max < mtx[i][j]:
                    max = mtx[i][j]
    print(max)


def sum_in_quaters():
    n = int(input())
    mtx = create_square_matrix_from_string(n)

    top_sum = 0
    right_sum = 0
    bottom_sum = 0
    left_sum = 0

    for i in range(n):
        for j in range(n):
            if i < j and i + j < n - 1:  # верхняя четверть
                top_sum += mtx[i][j]
            elif i < j and i + j > n - 1:  # правая четверть
                right_sum += mtx[i][j]
            elif i > j and i + j > n - 1:  # нижняя четверть
                bottom_sum += mtx[i][j]
            elif i > j and i + j < n - 1:  # левая четверть
                left_sum += mtx[i][j]

    print("Верхняя четверть: ", top_sum)
    print("Правая четверть: ", right_sum)
    print("Нижняя четверть: ", bottom_sum)
    print("Левая четверть: »", left_sum)


def mul_table():
    n = int(input())
    m = int(input())
    mtx = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mtx[i][j] = i * j
    res = ""
    for i in range(n):
        for j in range(m):
            res += str(mtx[i][j]) + " "
        res += "\n"
    return res

def max_value_in_mtx(mtx):
    max = mtx[0][0]
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if max < mtx[i][j]:
                max = mtx[i][j]
    return max


def index_max_value_in_table():
    n = int(input())
    m = int(input())
    mtx = [[int(num) for num in input().split()] for _ in range(n)]
    max = max_value_in_mtx(mtx)
    for i in range(n):
        for j in range(m):
            if mtx[i][j] == max:
                return str(i) + " " + str(j)


def swap_column():
    n = int(input())
    m = int(input())
    mtx = [[int(num) for num in input().split()] for _ in range(n)]
    k = int(input())
    l = int(input())

    for i in range(n):
        temp = mtx[i][l]
        mtx[i][l] = mtx[i][k]
        mtx[i][k] = temp

    res = ""
    for i in range(n):
        for j in range(m):
            res += str(mtx[i][j]) + " "
        res += "\n"
    return res


def is_symmetrical():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    flag = 1
    for i in range(1,n):
        for j in range(0,i):
            print(mtx[i][j],mtx[j][i])
            if mtx[i][j] != mtx[j][i]:
                flag = 0
    if flag:
        print("YES")
    else:
        print("NO")

is_symmetrical()