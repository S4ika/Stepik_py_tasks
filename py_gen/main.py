import josephus_problem, coordinate_quarters, more_than_previous, swap_neighbour,\
    developmental_shift, various_elements, mul_dig, rock_paper_scissors,rock_paper_scissors_lizard_spok,\
    o_and_p,sillicon_valley,roscomnadzor, pascal_triangle, packing_duplicates, chunky


def tasks():
    print("1. Задача Иосифа Флавия")
    print("2. Координатные четверти")
    print("3. Больше чем предыдущее")
    print("4. Назад, вперёд и наоборот")
    print("5. Сдвиг в развитии")
    print("6. Различные элементы")
    print("7. Произведение чисел")
    print("8. Камень, ножницы, бумага")
    print("9. Камень, ножницы, бумага, ящерица, Спок ")
    print("10. Орел и Решка")
    print("11. Кремниевая долина")
    print("12. Роскомнадзор запретил букву а")
    print("13. Треугольник Паскаля (выводим n-й уровень)")
    print("14. Треугольник Паскаля")
    print("15. Упаковка дупликатов")
    print("16. Разбиение на чанки")


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
        case 7:
            mul_dig.mul_dig()
        case 8:
            rock_paper_scissors.start_game()
        case 9:
            rock_paper_scissors_lizard_spok.start_game()
        case 10:
            o_and_p.counter_p()
        case 11:
            sillicon_valley.find_anton()
        case 12:
            roscomnadzor.opyat_etot_()
        case 13:
            pascal_triangle.n_level()
        case 14:
            pascal_triangle.pascal_triangle()
        case 15:
            packing_duplicates.pack()
        case 16:
            chunky.run()
        case _:
            print("Такой задачи нет =(")


if __name__ == '__main__':
    choice()