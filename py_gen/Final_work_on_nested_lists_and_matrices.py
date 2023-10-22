# Итоговая работа на вложенные списки и матрицы

def create_square_matrix_from_string(size):
    matrix = []
    for _ in range(size):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix

def print_matrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=" ")
        print()

# Каждый n-ый элемент
# На вход программе подается строка текста, содержащая символы и число nn.
# Из данной строки формируется список. Напишите программу,
# которая разделяет список на вложенные подсписки так, что nn последовательных
# элементов принадлежат разным подспискам.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая символы,
# отделенные символом пробела и число nn на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести указанный вложенный список.
def each_n_th_element():
    lst = input().split()
    n = int(input())
    lists = [[] for _ in range(n)]
    counter = 0
    for i in lst:
        if counter == n:
            counter = 0
        lists[counter].extend(i)
        counter += 1
    return lists

def max_elem_below_side_diagonal():
    size = int(input())
    mtx = create_square_matrix_from_string(size)
    max_elem = mtx[0][size-1]
    for i in range(size):
        for j in range(size):
            if j >= size - i - 1:
                if max_elem < mtx[i][j]:
                    max_elem = mtx[i][j]
    return max_elem

def matrix_transpose():
    size = int(input())
    mtx = create_square_matrix_from_string(size)
    transpose_mtx = [[] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            transpose_mtx[j].append(mtx[i][j])
    return transpose_mtx

def snowflake():
    size = int(input())
    mtx = [["." for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == size // 2 or j == size // 2 or i == j or j == size - i - 1:
                mtx[i][j] = "*"
    return mtx

def is_symmetrical_side_diagonal():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    flag = 1
    for i in range(0,n):
        for j in range(0,n):
            if mtx[i][j] != mtx[n - j - 1][n - i - 1]:
                flag = 0
    if flag:
        print("YES")
    else:
        print("NO")

def check_string_contains_1_to_n_elems(lst, size):
    checker = 0
    for i in range(size):
        checker += i + 1
    for i in lst:
        checker -= i
    return checker == 0


def latinian_square():
    n = int(input())
    mtx = create_square_matrix_from_string(n)
    rows = [[ mtx[j][i] for j in range(n)] for i in range(n)]

    for i in range(n):
        if not check_string_contains_1_to_n_elems(mtx[i], n) or \
           not check_string_contains_1_to_n_elems(rows[i], n):
            print("NO")
            return
    print("YES")
    return

def queens_moves():
    queens_pos = input()
    size = 22
    kj = 7 + (ord(queens_pos[0]) - 97)
    ki = 7 + 7 -(int(queens_pos[1]) - 1)
    print(ki, kj)
    board = [["." for _ in range(size)] for _ in range(size)]
    board[ki][kj]= "Q"
    for i in range(7):
        for _ in range(7):
            board[ki + i + 1][kj] = "*"
            board[ki - i - 1][kj] = "*"
            board[ki][kj + i + 1] = "*"
            board[ki][kj - i - 1] = "*"
            board[ki - i - 1][kj - i - 1] = "*"
            board[ki - i - 1][kj + i + 1] = "*"
            board[ki + i + 1][kj - i - 1] = "*"
            board[ki + i + 1][kj + i + 1] = "*"
    result_mtx = [ board[i][7:15] for i in range(7,15)]

    print_matrix(result_mtx, len(result_mtx), len(result_mtx))


def diagonals_parallel_to_the_main_diagonal():
    n = int(input())
    mtx = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mtx[i][j] = abs(i-j)
    print_matrix(mtx, n, n)


def final_work_on_nexted_lists_and_matrics():
    print("1. Каждый n-ый элемент\n2. Максимальный в области 2\n3. Транспонирование матрицы\n4. Снежинка"
          "\n5. Симметричная матрица (относительно побочной диагонали)\n6. Латинский квадрат 🌶️"
          "\n7. Ходы ферзя\n8. Диагонали параллельные главной")
    var = int(input("Выбери необходимое задание : "))
    match var:
        case 1:
            print(each_n_th_element())
        case 2:
            print(max_elem_below_side_diagonal())
        case 3:
            mtx = matrix_transpose()
            print_matrix(mtx,len(mtx),len(mtx))
        case 4:
            mtx = snowflake()
            print_matrix(mtx, len(mtx), len(mtx))
        case 5:
            is_symmetrical_side_diagonal()
        case 6:
            latinian_square()
        case 7:
            queens_moves()
        case 8:
            diagonals_parallel_to_the_main_diagonal()
