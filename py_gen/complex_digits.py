def complex_nums_operators():
    n = complex(input())
    m = complex(input())
    print(f'{n} + {m} = {n + m}')
    print(f'{n} - {m} = {n - m}')
    print(f'{n} * {m} = {n * m}')

def abs_complex():
    numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j,
               -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
    numbers_abs = [abs(i) for i in numbers]
    print(max(numbers, key=abs))
    print(max(numbers_abs))


def conjugate_numbers():
    n = int(input())
    z1 = complex(input())
    z2 = complex(input())

    print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n+1))

conjugate_numbers()