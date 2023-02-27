import model_json as mdl

def show_menu_header():
    print('Программа для работы с заметками')
    print('--------------------------------')

def show_main_menu():
    return input(
        "1 - Показать весь список заметок\n2 - Добавить заметку\n3 - Найти заметку\n4 - Фильтровать заметки\n5 - Выход\n")

def show_selected_note_menu():
    return input(
        "1 - Редактировать заметку\n2 - Удалить заметку\n3 - Показать весь список\n4 - Выход\n")


def show_end_program():
    print('Завершение работы программы')

def show_notes_table():
    # отображение таблицы записей - notes

    #загружаем данные из файла json в словарь
    status, data = mdl.json_load_from_file()
    if status == False:
        print("Ошибка чтения файла json")
    else:
        # Выводим шапку
        print('id', 'header', 'text', 'created')
        # Выводим записи
        for item in data:
            print(item['id'], item['header'], item['txt'], item['created'])


def show_note_add():
    nid = input("Введите id заметки")
    input("Добавление заметки:")
    nheader = input("Введите заголовок заметки")
    ntxt =  input("Введите текст заметки")
    ncreated = datetime.datetime.now()
    nedited = ncreated

