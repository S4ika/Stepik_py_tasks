import math
import fractions
from fractions import Fraction

def fraction_reduce():
    n = int(input())
    m = int(input())
    print(Fraction(n, m))

def fraction_operations():
    n = input()
    m = input()
    print(f'{n} + {m} = {Fraction(n) + Fraction(m)}')
    print(f'{n} - {m} = {Fraction(n) - Fraction(m)}')
    print(f'{n} * {m} = {Fraction(n) * Fraction(m)}')
    print(f'{n} / {m} = {Fraction(n) / Fraction(m)}')

def sum_fractions_1():
    n = int(input())
    result = Fraction('0')
    for i in range(1, n + 1):
        result += Fraction(f'1/{i ** 2}')
    print(result)

def sum_fraction_2():
    n = int(input())
    result = Fraction('0')
    for i in range(1, n + 1):
        result += Fraction(f'1/{math.factorial(i)}')
    print(result)

def young_mathematics():
    n = int(input())
    maximum = Fraction(f'1/{n - 1}')
    for i in range(2,n-1):
        fr = Fraction(f'{i}/{n - i}')
        if fr > maximum and fr.numerator < fr.denominator and math.gcd(i,n-i) == 1:
            maximum = fr
    print(maximum)

def sorted_fractions():
    n = int(input())
    list_fractions = []
    for i in range(1,n):
        for j in range(n,1,-1):
            if Fraction(f'{i}/{j}') < 1 and Fraction(f'{i}/{j}') not in list_fractions:
                list_fractions.append(Fraction(f'{i}/{j}'))
    for i in sorted(list_fractions):
        print(i)


sorted_fractions()