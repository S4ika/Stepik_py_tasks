def create_square_mtx():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    return mtx

def sum_diagonal_elems(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


def print_matrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=" ")
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
    mtx = create_square_mtx()
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
    mtx = create_square_mtx()
    for i in range(len(mtx)):
        avg = avg_value_in_list(mtx[i])
        counter = 0
        for j in range(len(mtx)):
            if mtx[i][j] > avg:
                counter += 1
        print(counter)

def max_below_main_diagonal():
    mtx = create_square_mtx()
    n = len(mtx)
    max = mtx[0][0]
    for i in range(n):
        for j in range(0,i+1):
            if max < mtx[i][j]:
                max = mtx[i][j]
    print(max)

def max_in_area():
    mtx = create_square_mtx()
    n = len(mtx)
    max = mtx[0][0]
    for i in range(n):
        for j in range(0, n):
            if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j) or (i == j) or (i + j + 1 == n):
                if max < mtx[i][j]:
                    max = mtx[i][j]
    print(max)


def sum_in_quaters():
    mtx = create_square_mtx()
    n = len(mtx)
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
    mtx = create_square_mtx()
    flag = 1
    n = len(mtx)
    for i in range(1,n):
        for j in range(0,i):
            print(mtx[i][j],mtx[j][i])
            if mtx[i][j] != mtx[j][i]:
                flag = 0
    if flag:
        print("YES")
    else:
        print("NO")


def swap_diagonals_in_mtx(mtx):
    n = len(mtx)
    for i in range(n):
        temp = mtx[i][i]
        mtx[i][i] = mtx[n-1-i][i]
        mtx[n-1-i][i] = temp

    return mtx


def swap_diagonals():
    mtx = create_square_mtx()
    mtx_swap = swap_diagonals_in_mtx(mtx)
    print_matrix(mtx_swap,len(mtx),len(mtx))


def up_and_down():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    count_iter = n // 2 + n % 2
    for i in range(count_iter):
        for j in range(n):
            temp = mtx[i][j]
            mtx[i][j] = mtx[n - 1 - i][j]
            mtx[n - 1 - i][j] = temp

    print_matrix(mtx, n, n)

def rotate_matrix():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    res_mtx = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res_mtx[i].append(mtx[n-1-j][i])
    print_matrix(res_mtx, n, n)


def horse_attack():
    size = 8
    horse_pos = input()
    kj = ord(horse_pos[0]) - 97 + 1
    ki = size - int(horse_pos[1]) + 1
    b = [['.'] * 12 for i in range(12)]
    moves = [1, 2, 1, -2, -1, 2, -1, -2, 2, 1, 2, -1, -2, 1, -2, -1]
    ki += 1
    kj += 1
    for ii in range(0, 16, 2):
        i = ki + moves[ii]
        j = kj + moves[ii + 1]
        b[i][j] = '*'
    b[ki][kj] = 'N'
    for i in range(2, 10):
        for j in range(2, 10):
            if (j == 9):
                print(b[i][j])
            else:
                print(b[i][j], end=' ')


def sum_elems_in_line(line):
    sum = 0
    for i in line:
        sum += i
    return sum

def check_elems_in_magic_square(mtx):
    digits = [i+1 for i in range(len(mtx) * len(mtx))]
    list_temp = []
    for i in range(len(mtx)):
        list_temp.extend(mtx[i])
    list_temp.sort()
    return digits == list_temp

def magic_square_check(mtx):
    flag = 1
    t = sum_elems_in_line(mtx[0])
    t1 = []
    t2 = []
    t3 = []
    for i in range(len(mtx)):
        if sum_elems_in_line(mtx[i]) != t:
            flag = 0
            break
        t1.append(mtx[i][0])
        t2.append(mtx[i][1])
        t3.append(mtx[i][2])
    print(sum_elems_in_line(t1))
    print(sum_diagonal_elems(mtx))
    if sum_elems_in_line(t1) != t or sum_elems_in_line(t2) != t or sum_elems_in_line(t3) != t or \
            sum_diagonal_elems(mtx) != t or sum_diagonal_elems(swap_diagonals_in_mtx(mtx)) != t:
                    flag = 0
    return flag == 1


def magic_square():
    mtx = create_square_mtx()
    if check_elems_in_magic_square(mtx) and magic_square_check(mtx) :
        print("YES")
    else:
        print("NO")


def chess_board():
    # Вводим размер доски
    n, m = map(int, input().split())
    sign = {True: ".", False: "*"}
    flag = True
    board = [["" for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            board[i][j] = sign[flag]
            flag = not flag
        if board[i][0] != sign[not flag]:
            flag = not flag
    print_matrix(board, n, m)


def side_diagonal():
    n = int(input())
    mtx = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == n - 1 - j:
                mtx[i][j] = 1
            if i + j >= n:
                mtx[i][j] = 2

    print_matrix(mtx, n, n)

def fill_matrix():
    n,m = map(int,input().split())
    mtx = [[0 for _ in range(m)] for _ in range(n)]
    counter = 1
    for i in range(n):
        for j in range(m):
            mtx[i][j] = counter
            counter += 1
    print_matrix(mtx, n, m)

fill_matrix()