def timur_and_team():
    n = int(input())
    m = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    return n + m + k - x - y + z

def summer_books():
    n = int(input())
    m = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    t = int(input())
    a = int(input())
    n_m = n + m - x - t
    m_k = m + k - y - t
    n_k = n + k - z - t

    only_n = n - t - n_m - n_k
    only_m = m - t - n_m - m_k
    only_k = k - t - n_k - m_k

    only_one_book = only_k + only_m + only_n

    two_book = n_m + n_k + m_k

    noone_book = a - t - only_one_book - two_book

    print(only_one_book)
    print(two_book)
    print(noone_book)


def count_different_simb():
    input_set = set(input())
    print(len(input_set))

def unique_digits():
    input_digits = input()
    set_digits = set(input_digits)
    if len(input_digits) == len(set_digits):
        print("YES")
    else:
        print("NO")

def all_ten_digits():
    input_digits_1 = input()
    input_digits_2 = input()
    if len(set(input_digits_1 + input_digits_2)) == 10:
        print("YES")
    else:
        print("NO")

def same_sets():
    input_digits_1 = set(input())
    input_digits_2 = set(input())
    if input_digits_1 == input_digits_2:
        print("YES")
    else:
        print("NO")

def same_letters_in_three_words():
    word_1, word_2, word_3 = input().split()
    if set(word_1) == set(word_2) and set(word_1) == set(word_3) and set(word_3) == set(word_2):
        print("YES")
    else:
        print("NO")

def unique_symb_1():
    n = int(input())
    result_lst = []
    for _ in range(n):
        result_lst.append(len(set(input().lower())))
    for i in result_lst:
        print(i)

def unique_symb_2():
    n = int(input())
    all_words = ""
    for _ in range(n):
        all_words += input().lower()
    print(len(set(all_words)))

def count_words():
    input_words = input().lower().split()
    output_set = set()
    for i in range(len(input_words)):
        t = input_words[i]
        if t[-1] == "," or t[-1] == "." or t[-1] == ";":
             t = t[:len(t) - 1]
        if t[0] == "," or t[0] == "." or t[0] == ";" or t[0] == ":" or t[0] == "-" or \
           t[0] == "?" or t[0] == "!":
             t = t[1:]
        output_set.add(t)
    print(len(output_set))

def is_this_number_in_the_set():
    input_str = input().split()
    our_set = set()
    for i in input_str:
        if int(i) in our_set:
            print("YES")
        else:
            print("NO")
        our_set.add(int(i))


def lenght_union_sets():
    set_1 = set(input().split())
    set_2 = set(input().split())
    print(len(set_1 & set_2))


def sorted_union():
    set_1 = set(int(i) for i in input().split())
    set_2 = set(int(i) for i in input().split())
    sorted_list = sorted(set_1 & set_2)
    result = ""
    for i in sorted_list:
        result += str(i) + " "
    print(result[:-1])


def sorted_dif():
    set_1 = set(int(i) for i in input().split())
    set_2 = set(int(i) for i in input().split())
    sorted_list = sorted(set_1 - set_2)
    res = ""
    for i in sorted_list:
        res += str(i) + " "
    print(res[:-1])


def same_dig_in_strings():
    n = int(input())
    input_set = set(map(int, set(input())))
    for i in range(n - 1):
        new_input_set = set(map(int, set(input())))
        input_set &= new_input_set
    res = ""
    sorted_list = sorted(input_set)
    for i in sorted_list:
        res += str(i) + " "
    print(res[:-1])


def same_digits_in_two_numbers():
    input_set_1 = set(map(int, set(input())))
    input_set_2 = set(map(int, set(input())))
    if input_set_1.isdisjoint(input_set_2):
        print("NO")
    else:
        print("YES")

def check_superset():
    input_set_1 = set(map(int, set(input())))
    input_set_2 = set(map(int, set(input())))
    if input_set_1.issuperset(input_set_2):
        print("YES")
    else:
        print("NO")

def informatica_lesson():
    input_set_1 = set(map(int, input().split()))
    input_set_2 = set(map(int, input().split()))
    input_set_3 = set(map(int, input().split()))
    result_list = sorted((input_set_1 & input_set_2) - input_set_3, reverse=True)
    r = ""
    for i in result_list:
        r += str(i) + " "
    print(r[:-1])


def math_lesson():
    input_set_1 = set(map(int, input().split()))
    input_set_2 = set(map(int, input().split()))
    input_set_3 = set(map(int, input().split()))
    result_list = sorted(((input_set_1 | input_set_2 | input_set_3) - (input_set_1 & input_set_2 & input_set_3)))
    r = ""
    for i in result_list:
        r += str(i) + " "
    print(r[:-1])

def physics_lesson():
    input_set_1 = set(map(int, input().split()))
    input_set_2 = set(map(int, input().split()))
    input_set_3 = set(map(int, input().split()))
    result_list = sorted((input_set_3 - input_set_1 - input_set_2), reverse=True)
    r = ""
    for i in result_list:
        r += str(i) + " "
    print(r[:-1])

def biology_lesson():
    input_set_1 = set(map(int, input().split()))
    input_set_2 = set(map(int, input().split()))
    input_set_3 = set(map(int, input().split()))
    universum = set(range(11))
    result_list = sorted((universum - (input_set_3 | input_set_1 | input_set_2)))
    r = ""
    for i in result_list:
        r += str(i) + " "
    print(r[:-1])
