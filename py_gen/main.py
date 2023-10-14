import Final_work_on_nested_lists_and_matrices
import dictionaries
import josephus_problem, coordinate_quarters, more_than_previous, swap_neighbour,\
    developmental_shift, various_elements, mul_dig, rock_paper_scissors,rock_paper_scissors_lizard_spok,\
    o_and_p,sillicon_valley,roscomnadzor, pascal_triangle, packing_duplicates, chunky, sublists, matrix
import sets
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
    print("47. Итоговая работа на вложенные списки и матрицы")
    print("48. Тимур и его команда")
    print("49. Книги на прочтение 🌶️")
    print("50. Количество различных символов")
    print("51. Неповторимые цифры")
    print("52. Все 10 цифр")
    print("53. Одинаковые наборы")
    print("54. Три слова")
    print("55. Уникальные символы 1")
    print("56. Уникальные символы 2")
    print("57. Количество слов в тексте")
    print("58. Встречалось ли число раньше?")
    print("59. Количество совпадающих")
    print("60. Общие числа")
    print("61. Числа первой строки")
    print("62. Общие цифры")
    print("63. Одинаковые цифры")
    print("64. Все цифры")
    print("65. Урок информатики")
    print("66. Урок математики")
    print("67. Урок физики")
    print("68. Урок биологии")
    print("69. Строковое представление")
    print("70. Информация об учебных курсах")
    print("71. Набор сообщений")
    print("72. Код Морзе")
    print("73. Самое редкое слово 🌶️")
    print("74. Исправление дубликатов 🌶️")
    print("75. Словарь программиста")
    print("76. Анаграммы 1")
    print("77. Анаграммы 2")
    print("78. Словарь синонимов")
    print("79. Страны и города")
    print("80. Телефонная книга")
    print("81. Секретное слово")


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
        case 47:
            Final_work_on_nested_lists_and_matrices.final_work_on_nexted_lists_and_matrics()
        case 48:
            print(sets.timur_and_team())
        case 49:
            sets.summer_books()
        case 50:
            sets.count_different_simb()
        case 51:
            sets.unique_digits()
        case 52:
            sets.all_ten_digits()
        case 53:
            sets.same_sets()
        case 54:
            sets.same_letters_in_three_words()
        case 55:
            sets.unique_symb_1()
        case 56:
            sets.unique_symb_2()
        case 57:
            sets.count_words()
        case 58:
            sets.is_this_number_in_the_set()
        case 59:
            sets.lenght_union_sets()
        case 60:
            sets.sorted_union()
        case 61:
            sets.sorted_dif()
        case 62:
            sets.same_dig_in_strings()
        case 63:
            sets.same_digits_in_two_numbers()
        case 64:
            sets.check_superset()
        case 65:
            sets.informatica_lesson()
        case 66:
            sets.math_lesson()
        case 67:
            sets.physics_lesson()
        case 68:
            sets.biology_lesson()
        case 69:
            dictionaries.string_representation()
        case 70:
            dictionaries.training_courses_information()
        case 71:
            dictionaries.message_typing()
        case 72:
            dictionaries.morse_code()
        case 73:
            dictionaries.rarest_word()
        case 74:
            dictionaries.correcting_duplicates()
        case 75:
            dictionaries.program_dictionary()
        case 76:
            dictionaries.anagrams_1()
        case 77:
            dictionaries.anagrams_2()
        case 78:
            dictionaries.synonym_dictionary()
        case 79:
            dictionaries.countries_and_cities()
        case 80:
            dictionaries.phone_book()
        case 81:
            dictionaries.secret_word()
        case _:
            print("Такой задачи нет =(")


if __name__ == '__main__':
    choice()