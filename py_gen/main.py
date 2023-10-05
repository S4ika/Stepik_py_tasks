import josephus_problem, coordinate_quarters, more_than_previous, swap_neighbour,\
    developmental_shift, various_elements, mul_dig, rock_paper_scissors,rock_paper_scissors_lizard_spok,\
    o_and_p,sillicon_valley,roscomnadzor, pascal_triangle, packing_duplicates, chunky, sublists, matrix
import tuples


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
    print("17. Подсписки списка")
    print("18. Ввод и вывод матрицы")
    print("19. След матрицы")
    print("20. Больше среднего")
    print("21. Максимальный элемент ниже(или находится на) главной диагонали")
    print("22. Суммы четвертей матрицы")
    print("23. Таблица умножения")
    print("24. Максимум в таблице(индексы первого вхождения)")
    print("25. Обмен столбцов")
    print("26. Симметричная матрица")
    print("27. Обмен диагоналей")
    print("28. Зеркальное отображение")
    print("29. Поворот матрицы")
    print("30. Ходы коня")
    print("31. Шахматная доска")
    print("32. Побочная диагональ")
    print("33. Заполнение 1")
    print("34. Заполнение 2")
    print("35. Заполнение 3")
    print("36. Заполнение 4")
    print("37. Заполнение 5")
    print("38. Заполнение змейкой")
    print("39. Заполнение диагоналями")
    print("40. Заполнение спиралью")
    print("41. Сложение матриц")
    print("42. Умножение матриц 🌶️")
    print("43. Возведение матрицы в степень 🌶️")
    print("44. Вершина параболы")
    print("45. Конкурсный отбор")
    print("46. Последовательность Трибоначчи")


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
        case 17:
            sublists.run()
        case 18:
            matrix.create_and_print_matrix()
        case 19:
            matrix.create_square_matrix_and_sum_diagonal_elems()
        case 20:
            matrix.more_than_avg()
        case 21:
            matrix.max_below_main_diagonal()
        case 22:
            matrix.sum_in_quaters()
        case 23:
            matrix.mul_table()
        case 24:
            matrix.index_max_value_in_table()
        case 25:
            matrix.swap_column()
        case 26:
            matrix.is_symmetrical()
        case 27:
            matrix.swap_diagonals()
        case 28:
            matrix.up_and_down()
        case 29:
            matrix.rotate_matrix()
        case 30:
            matrix.horse_attack()
        case 31:
            matrix.chess_board()
        case 32:
            matrix.side_diagonal()
        case 33:
            matrix.fill_matrix()
        case 34:
            matrix.fill_matrix_verical()
        case 35:
            matrix.fill_matrix_zeroes_and_ones()
        case 36:
            matrix.fill_matrix_like_sand_clock()
        case 37:
            matrix.fill_matrix_with_shift()
        case 38:
            matrix.snake_fill_matrix()
        case 39:
            matrix.filling_with_diagonals()
        case 40:
            matrix.filling_with_spiral_fast()
        case 41:
            matrix.sum_matrix_task()
        case 42:
            matrix.mul_task()
        case 43:
            matrix.power_matrix()
        case 44:
            tuples.top_of_parabola()
        case 45:
            tuples.competitive_selection()
        case 46:
            tuples.print_tribonacci_sequence()
        case _:
            print("Такой задачи нет =(")


if __name__ == '__main__':
    choice()