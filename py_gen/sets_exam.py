#Итоговая работа по множествам


def homework():
    n = int(input())
    m = int(input())
    k = int(input())
    p = int(input())
    return n - (m + k - p)


def voshod():
    degrees = [int(i) for i in input().split()]
    len_set = len(set(degrees))
    len_list = len(degrees)
    return len_list - len_set


def cities():
    n = int(input())
    cities_set = set()
    for i in range(n + 1):
        city = input()
        if city in cities_set:
            return "REPEAT"
        cities_set.add(city)
    return "OK"


def books():
    m = int(input())
    n = int(input())
    books = set()
    for i in range(m):
        book = input()
        books.add(book)
    for i in range(n):
        book = input()
        if book in books:
            print("YES")
        else:
            print("NO")


def strange_hobby():
    first_task = set([int(i) for i in input().split()])
    second_task = set([int(i) for i in input().split()])
    dig_in_two_tasks = first_task & second_task
    if len(dig_in_two_tasks) != 0:
        print(*sorted(dig_in_two_tasks, reverse=True))
    else:
        print("BAD DAY")


def online_school_beegeek_1():
    test = set([int(i) for i in input().split()])
    answer = set([int(i) for i in input().split()])
    if test == answer:
        print("YES")
    else:
        print("NO")


def online_school_beegeek_2():
    m = int(input())
    n = int(input())
    set_math = set()
    for i in range(m):
        surname = input()
        set_math.add(surname)
    for i in range(n):
        surname = input()
        set_math.discard(surname)
    print(len(set_math))


def online_school_beegeek_3():
    m = int(input())
    n = int(input())
    set_math = set()
    set_cs = set()
    for i in range(m):
        surname = input()
        set_math.add(surname)
    for i in range(n):
        surname = input()
        set_cs.add(surname)
    if len(set_math.symmetric_difference(set_cs)) == 0:
        print("NO")
    else:
        print(len(set_math.symmetric_difference(set_cs)))


def online_school_beegeek_4():
    student_set = set()
    head = [student_set.add(i) for i in input().split()]
    assistant = [student_set.add(i) for i in input().split()]
    print(*sorted(student_set))


def online_school_beegeek_5():
    m = int(input())
    n = int(input())
    set_one_subject = set()
    for i in range(n + m):
        surname = input()
        if surname in set_one_subject:
            set_one_subject.discard(surname)
        else:
            set_one_subject.add(surname)
    if len(set_one_subject) == 0:
        print("NO")
    else:
        print(len(set_one_subject))


def online_school_beegeek_6():
    m = int(input())
    flag = False
    set_students = set()
    for i in range(m):
        n = int(input())
        one_lesson = set()
        for j in range(n):
            username = input()
            one_lesson.add(username)
        if not flag:
            set_students = one_lesson.copy()
            flag = True
        else:
            set_students = set_students.intersection(one_lesson)
    perfect_students = sorted(set_students)
    for i in perfect_students:
        print(i)
