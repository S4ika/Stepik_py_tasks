import re

def string_representation():
    num_to_str = dict(zip([str(i) for i in range(10)],\
                      ("zero","one","two","three","four","five","six","seven","eight","nine")))
    num = input()
    result = []
    for i in num:
        result.append(num_to_str[i])
    print(*result)

def training_courses_information():
    courses = {'CS101': {'audience_number': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
             'CS102': {'audience_number': '4501', 'teacher': 'Альварадо', 'time': '9:00'},
             'CS103': {'audience_number': '6755', 'teacher': 'Рич', 'time': '10:00'},
             'NT110': {'audience_number': '1244', 'teacher': 'Берк', 'time': '11:00'},
             'CM241': {'audience_number': '1411', 'teacher': 'Ли', 'time': '13:00'}}
    input_course = input()
    if input_course in courses:
        print(f'{input_course}: {courses[input_course]["audience_number"]}, {courses[input_course]["teacher"]}, {courses[input_course]["time"]}')

def message_typing():
    message = input().replace("\"","'").upper()
    keys_symb = {
        "1": ".,?!:",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
        "0": " "
    }
    result = ""
    for i in message:
        for j in keys_symb.items():
            if i in j[1]:
                result += j[0] * (j[1].index(i) + 1)
    print(result)

def morse_code():
    morze_codes = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
    input_text = input().upper()
    res = []
    for l in input_text:
        if l not in ' !@#$%^&*()_+-=,.<>|\\/?':
            res.append(morze_codes[l])
    print(*res)

def rarest_word():
    lst = [word.strip('.,!?:;-') for word in input().lower().split()]
    dict_1 = {}
    for i in lst:
        dict_1[i] = dict_1.get(i, 0) + 1

    min_key = lst[0]
    for k, v in dict_1.items():
        if v < dict_1[min_key] or (v == dict_1[min_key] and k < min_key):
            min_key = k
    print(min_key)

def correcting_duplicates():
    input_str = input().split()
    symb_dict = {}.fromkeys(input_str,0)
    result = []
    for i in input_str:
        if symb_dict[i] > 0:
            result.append(i+f"_{symb_dict[i]}")
        else:
            result.append(i)
        symb_dict[i] += 1
    print(*result)

def program_dictionary():
    n = int(input())
    dict_p = {}
    for i in range(n):
        input_text = input().split(": ")
        dict_p[input_text[0].lower()] = input_text[1]
    m = int(input())
    for i in range(m):
        input_word = input()
        print(dict_p.get(input_word.lower(), "Не найдено"))

def anagrams_1():
    input_text_1 = input()
    input_text_2 = input()
    dict_1 = {}
    dict_2 = {}
    for i in input_text_1:
        dict_1[i] = dict_1.get(i,0) + 1
    for i in input_text_2:
        dict_2[i] = dict_2.get(i,0) + 1
    if dict_1 == dict_2:
        print("YES")
    else:
        print("NO")

def anagrams_2():
    input_text_1 = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?, ]", "", input().lower())
    input_text_2 = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?, ]", "", input().lower())
    dict_1 = {}
    dict_2 = {}

    for i in input_text_1:
        dict_1[i] = dict_1.get(i, 0) + 1
    for i in input_text_2:
        dict_2[i] = dict_2.get(i, 0) + 1
    if dict_1 == dict_2:
        print("YES")
    else:
        print("NO")

def synonym_dictionary():
    n = int(input())
    dict_synonims = {}
    for i in range(n):
        input_text = input().split()
        dict_synonims[input_text[0]] = input_text[1]
    word = input()
    for k,v in dict_synonims.items():
        if k == word:
            print(v)
        elif v == word:
            print(k)

def countries_and_cities():
    n = int(input())
    dict_c = {}
    for i in range(n):
        input_info = input().split()
        dict_c[input_info[0]] = input_info[1:]
    m = int(input())
    for i in range(m):
        city = input()
        for key,value in dict_c.items():
            if city in value:
                print(key)

def phone_book():
    n = int(input())
    phone_book = {}
    for i in range(n):
        person_tel = input().split()
        phone_book[person_tel[1].lower()] = phone_book.get(person_tel[1].lower(),[])
        phone_book[person_tel[1].lower()].append(person_tel[0])
    m = int(input())
    for i in range(m):
        name = input()
        print(*phone_book.get(name,"абонент не найден"))

def secret_word():
    secret_word = input()
    dict_secret_l = {}
    for i in secret_word:
        dict_secret_l[i] = dict_secret_l.get(i, 0) + 1
    n = int(input())
    letters = {}
    for i in range(n):
        input_test = input().split(": ")
        letters[input_test[0]] = int(input_test[1])
    result = ""
    for i in secret_word:
        for k_1,v_1 in letters.items():
            if dict_secret_l[i] == v_1:
                result += k_1
    print(result)
