import josephus_problem


def tasks():
    print("1. Задача Иосифа Флавия")


def choice():
    tasks()
    print("Выбери необходимое задание : ")
    var = int(input())
    if var == 1:
        print(josephus_problem.josephus_problem())
    else:
        print("Такой задачи нет =(")

if __name__ == '__main__':
    choice()