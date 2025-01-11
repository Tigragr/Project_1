from file_operation import file_matrix, add_to_file, file_rewrite

def q_space(l):
    q = 0
    if l == 0:
        q = 1
    while l:
        if l:
            q += 1
        l = l // 10
    return q

def add_book(new_row):
    new_note = "\n" + ";".join(new_row)
    add_to_file(new_note)

def view_on_disp(choice, find_word):

    j = 0
    l_cell = [50, 35, 15, 18, 12]
    if find_word == '' and choice == '':
        print("Вы ничего не ввели. Показан весь каталог:")
        choice = 0

    len_file = len(file_matrix())
    q_f = q_space(len_file)

    print("   " + "-" * 144)
    print(f"   | № п/п{(q_f - 1) * ' '}|{18 * ' '}Название книги{18 * ' '}|{15 * ' '}Автор{15 * ' '}|  Год издания  |{7 * ' '}Жанр{7 * ' '}| Количество |")
    print("   " + "-" * 144)

    for str_of_catalog in file_matrix():

            if find_word in str_of_catalog[choice]:

                q_j = q_space(j+1)
                print(f"   |  {str(j + 1)}{(3 + q_f - q_j) * ' '}|", end='')
                j += 1
                str_for_prnt = ''

                for i in range(len(str_of_catalog)):
                      tab = l_cell[i] - 5 - len(str_of_catalog[i])
                      str_for_prnt += 5 * " " + str_of_catalog[i] + tab * " " + "|"

                print(str_for_prnt)

    print("   " + "-" * 144)

def view_for_edi_del(choice, find_word):

    id = 0
    l_cell = [50, 35, 15, 18, 12]
    if find_word == '' and choice == '':
        print("Вы ничего не ввели. Показан весь каталог:")
        choice = 0

    len_file = len(file_matrix())
    q_f = q_space(len_file)

    print("   " + "-" * 144)
    print(f"   |  Ключ{(q_f - 1) * ' '}|{18 * ' '}Название книги{18 * ' '}|{15 * ' '}Автор{15 * ' '}|  Год издания  |{7 * ' '}Жанр{7 * ' '}| Количество |")
    print("   " + "-" * 144)

    for str_of_catalog in file_matrix():
        id += 1

        if find_word in str_of_catalog[choice] or find_word.capitalize() in str_of_catalog[choice] or find_word.lower() in str_of_catalog[choice]:

            q_j = q_space(id)
            print(f"   |  {id}{(3 + q_f - q_j) * ' '}|", end='')

            str_for_prnt = ''

            for i in range(len(str_of_catalog)):
                  tab = l_cell[i] - 5 - len(str_of_catalog[i])
                  str_for_prnt += 5 * " " + str_of_catalog[i] + tab * " " + "|"

            print(str_for_prnt)

    print("   " + "-" * 144)

def edit_katal(key_note: int) ->None:

    print("Для изменения выбранной записи в каталоге внесите новые данные:")
    new_note = []
    for inp in ["название", "автора", "год издания", "жанр", "количество экземпляров"]:
        new_note.append(input(f"      - введите {inp} книги... "))

#    print(60 * "_")

    lst_katalog = file_matrix()

    lst_katalog.pop(key_note - 1)
    lst_katalog.insert(key_note - 1,new_note)

    new_str_for_file = ''
    for row in lst_katalog:
        new_str_for_file += ';'.join(row) + '\n'
    new_str_for_file = new_str_for_file[:-1]

    file_rewrite(new_str_for_file)

    print(60 * "_")

    print("Изменение записи произведено успешно!")

def del_katal(key_note: int) ->None:

    #    print(60 * "_")

    lst_katalog = file_matrix()

    lst_katalog.pop(key_note - 1)

    new_str_for_file = ''
    for row in lst_katalog:
        new_str_for_file += ';'.join(row) + '\n'
    new_str_for_file = new_str_for_file[:-1]

    file_rewrite(new_str_for_file)

    print(60 * "_")

    print("Удаление записи произведено успешно!")
