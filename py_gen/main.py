import josephus_problem, coordinate_quarters


def tasks():
    print("1. Задача Иосифа Флавия")
    print("2. Координатные четверти")


def choice():
    tasks()
    var = int(input("Выбери необходимое задание : "))
    match var :
        case 1:
            print(josephus_problem.josephus_problem())
        case 2:
            coordinate_quarters.coordinate_qtrs()
        case _:
            print("Такой задачи нет =(")


if __name__ == '__main__':
    choice()