#Итоговая работа по словарям

def genetics():
    dnk_to_rnk = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    input_dnk = input()
    output_rnk = ""
    for i in input_dnk:
        output_rnk += dnk_to_rnk[i]
    print(output_rnk)


def sequence_number():
    input_sting = input().split()
    counter_dict = {}
    result = ""
    for i in input_sting:
        num = counter_dict.get(i, 1)
        if num == 1:
            counter_dict[i] = 1
        result += str(num) + " "
        counter_dict[i] += 1
    print(result[:-1])


def scrabble_game():
    scrabble = {
        ('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'): 1,
        ('D', 'G'): 2,
        ('B', 'C', 'M', 'P'): 3,
        ('F', 'H', 'V', 'W', 'Y'): 4,
        ('K',): 5,
        ('J', 'X'): 8,
        ('Q', 'Z'): 10
    }
    input_word = input()
    result = 0
    for i in input_word:
        for k,v in scrabble.items():
            if i in k:
                result += v
    print(result)


def build_query_string(kwargs):
    sorted_kwargs = sorted(kwargs)
    result = ""

    for k in sorted_kwargs:
        result += k + "=" + str(kwargs[k]) + "&"
    return result[:-1]


def merge(dicts):
    result = {}
    for d in dicts:
        for x in d:
            result.setdefault(x, set()).add(d[x])
    return result


def dangerous_virus():
    files = {}
    for i in range(int(input())):
        name, *operations = input().split()
        files[name] = operations
    for i in range(int(input())):
        operation, name = input().split()
        if operation == 'read':
            if 'R' in files[name]:
                print('OK')
            else:
                print('Access denied')
        elif operation == 'write':
            if 'W' in files[name]:
                print('OK')
            else:
                print('Access denied')
        elif operation == 'execute':
            if 'X' in files[name]:
                print('OK')
            else:
                print('Access denied')


def internet_shopping():
    d = {}
    for i in range(int(input())):
        a, b, c = input().split()
        d[a] = d.get(a, {})
        d[a][b] = d.get(a, {}).get(b, 0) + int(c)
    for i in sorted(d):
        print(f'{i}:', sep='\n')
        for k in sorted(d[i]):
            print(f'{k} {d[i][k]}', sep='\n')
