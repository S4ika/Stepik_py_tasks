import random
from string import *

def secret_friend():
    n = int(input())
    students = []
    for i in range(n):
        students.append(input())
    students_shuffle = students.copy()
    checker = False
    while checker != True:
        random.shuffle(students_shuffle)
        for i in range(n):
            if students[i] == students_shuffle[i]:
                break
            if students[i] != students_shuffle[i] and i == n-1:
                checker = True
    students_pair = dict(zip(students, students_shuffle))
    for k,v in students_pair.items():
        print(f'{k} - {v}')


def generate_password(l):
    symbols = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
    password = "".join([symbols[random.randint(0,len(symbols) - 1)] for _ in range(l)])
    return password

def generate_passwords(n,m):
    pass_list = []
    for _ in range(n):
        pass_list.append(generate_password(m))
    return pass_list

def pass_gen_1():
    n = int(input())
    m = int(input())
    result = generate_passwords(n,m)
    for i in result:
        print(i)

def pass_checker(password):
    lowercase_lit = False
    uppercase_lit = False
    digit = False
    for i in password:
        if i.isnumeric():
            digit = True
        if i.isupper():
            uppercase_lit = True
        if i.islower():
            lowercase_lit = True
    return digit & lowercase_lit & uppercase_lit

def generate_passwords_2(n,m):
    pass_list = []
    i = 0
    while i < n:
        password = generate_password(m)
        if pass_checker(password):
            pass_list.append(password)
            i += 1
    return pass_list

def pass_gen_2():
    n = int(input())
    m = int(input())
    result = generate_passwords_2(n, m)
    for i in result:
        print(i)

from fractions import Fraction

n = int(input())
result = Fraction('0')
for i in range(1,n + 1):
    result += Fraction(f'1/{i ** 2}')
print(result)