def top_of_parabola():
    a = int(input())
    b = int(input())
    c = int(input())
    x = -b / (2 * a)
    y = (4 * a * c - b * b)/ (4 * a)
    print((x,y))

def competitive_selection():
    n = int(input())
    classmates = []
    for _ in range(n):
        s = input().split()
        classmates.append(s)
    for i in classmates:
        print(" ".join(i))
    print()
    for i in classmates:
        if int(i[1]) > 3:
            print(" ".join(i))

def tribonacci_sequence():
    n = int(input())
    t1 = 1
    t2 = 1
    t3 = 1
    temp = [t1, t2, t3]
    if n < 4:
        return temp[:n]
    for _ in range(n - 3):
        t1, t2, t3 = t2, t3, t1 + t2 + t3
        temp.append(t3)
    return temp

def list_int_to_string(list_int):
    for i in range(len(list_int)):
        list_int[i] = str(list_int[i])
    return " ".join(list_int)


def print_tribonacci_sequence():
    print(list_int_to_string(tribonacci_sequence()))