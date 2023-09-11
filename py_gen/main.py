import josephus_problem, coordinate_quarters, more_than_previous, swap_neighbour,\
    developmental_shift, various_elements


def tasks():
    print("1. Задача Иосифа Флавия")
    print("2. Координатные четверти")
    print("3. Больше чем предыдущее")
    print("4. Назад, вперёд и наоборот")
    print("5. Сдвиг в развитии")
    print("6. Различные элементы")


def choice():
    tasks()
    var = int(input("Выбери необходимое задание : "))
    match var :
        case 1:
            josephus_problem.josephus_problem()
        case 2:
            coordinate_quarters.coordinate_qtrs()
        case 3:
            more_than_previous.count_digits_more_than_prev()
        case 4:
            swap_neighbour.swap_nghbr()
        case 5:
            developmental_shift.dvlpmntl_shift()
        case 6:
            various_elements.various_elements()
        case _:
            print("Такой задачи нет =(")


if __name__ == '__main__':
    choice()