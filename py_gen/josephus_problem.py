#n человек, пронумерованных числами от  1 до n, стоят в кругу. Они начинают считаться,
# каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего
# за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.

# Формат входных данных
# На вход программе подаются два числа
# n и k, записанные на отдельных строках.

# Формат выходных данных
# Программа должна вывести одно число – номер человека, который останется в кругу последним.
# def simple_log(num,base) -> int:
#     counter = 1
#     temp = base
#     while temp * base <= num:
#         temp *= base
#         counter += 1
#     return counter
#
def josephus_problem() -> int:
    n = int(input("Введите количество человек : "))
    k = int(input("Введите номер выбывающего человека : "))
    #"Черная метка" - номер следующего убитого солдата
    death_mark = k - 1
    #Создаем список живых солдатов
    list_soldiers = [i + 1 for i in range(n)]
    counter = 0
    while len(list_soldiers) != 1:

        if counter != death_mark:
            list_soldiers.append(list_soldiers.pop(0))
            counter += 1
        else:
            list_soldiers.pop(0)
            counter = 0
    return list_soldiers[0]