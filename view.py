from datetime import datetime
from tokenize import String

import model_json as mdl


def show_menu_header():
    print()
    print('Программа для работы с заметками')
    print('--------------------------------')


def show_main_input_menu():
    return input(
        "1 - Показать весь список заметок\n2 - Выход\n")


def show_input_menu_1():
    return input(
        "1 - Редактировать заметку\n2 - Добавить заметку\n3 - Удалить заметку\n4 - Найти заметку\n5 - Фильтровать заметки\n6 - Выход\n")


def show_input_menu_1_4():
    return input(
        "1 - Показать весь список\n2 - Повтор поиска\n3 - Выход\n")

def show_input_menu_1_5():
    return input(
        "1 - Фильтр по заголовку\n2 - Фильтр по тексту\n3 - Фильтр по дате\n4 - Показать весь список\n5 - Выход\n")


def show_end_program():
    print('Завершение работы программы')


def show_notes_table():
    # отображение таблицы записей - notes
    # загружаем данные из файла json в словарь
    status, data = mdl.json_load_from_file()
    if status == False:
        print("Ошибка чтения файла json")
    else:
        # Выводим шапку
        print()
        print("Заметки - Полный список")
        print_tbl(data['note'])

def show_note_edit():
    # Добавление новой заметки
    print()
    print("Редактирование заметки")
    print("-------------")

    nid = input('Введите id редактируемой заметки: ')
    if not nid.isdigit():
        print('Введенное значение id не является числом. Заметка не найдена!')
        return
    status, data = mdl.json_load_from_file()  # загружаем данные из json-файла
    if status == False:
        print(f'ошибка чтения json-файла')
        return False

    #находим редактируемую запись
    is_finded = False
    for item in data['note']:
        if str(item['id']) == nid:
            print('Редактируемая заметка')
            print_tbl([item])  # item помещаем в список, чтобы for смог его обработать
            is_finded = True
            break
    if not is_finded:
        print(f'Заметка с id={nid} не найдена')
        return False
    print()  # разделитель

    new_header = input("Введите заголовок заметки: ")
    new_text = input("Введите текст заметки: ")
    new_created = datetime.now().strftime("%d.%m.%y %H:%M")  # дата время создания
    #обновляем данные заметки в словаре
    item['header'] = new_header
    item['text'] = new_text
    item['created'] = new_created

    # сохраняем данные в json-файл
    status, message = mdl.json_write_to_file(data)
    if status == False:
        print(f'ошибка записи в json-файл: {message}')

def show_note_add():
    # Добавление новой заметки
    print()
    print("Добавление новой заметки")
    print("-------------")
    new_header = input("Введите заголовок заметки: ")
    new_text = input("Введите текст заметки: ")
    new_created = datetime.now().strftime("%d.%m.%y %H:%M")  # дата время создания

    # загружаем имеющиеся данные из json-файла
    status, data = mdl.json_load_from_file()
    if status == False:
        print(f'ошибка чтения json-файла')

    # вычисляем номер new_id = max(id)+1
    new_id = 1
    for item in data['note']:
        if item['id'] > new_id:
            new_id = item['id']
    new_id += 1

    # формируем словарь из данных новой записи
    new_note = {'id': new_id, 'header': new_header, 'text': new_text, 'created': new_created}
    data['note'].append(new_note)

    # сохраняем данные в json-файл
    status, message = mdl.json_write_to_file(data)
    if status == False:
        print(f'ошибка записи в json-файл: {message}')


def show_note_delete():
# Удаление заметки по id
    print()
    print("Удаление заметки")
    print("-------------")
    nid = input('Введите id удаляемой заметки: ')
    if not nid.isdigit():
        print('Введенное значение id не является числом. Удаление заметки прервано!')
        return
    status, data = mdl.json_load_from_file()  # загружаем данные из json-файла
    if status == False:
        print(f'ошибка чтения json-файла')

    is_finded = False

    for i in range(len(data['note'])):
        if str(data['note'][i]['id']) == nid:
            del data['note'][i]     #удаление словаря заметки
            is_finded = True
            break

    if not is_finded:
        print(f'Заметка с id={nid} не найдена!')

    else:
        # сохраняем изменные данные в json-файл
        status, message = mdl.json_write_to_file(data)
        if status:
            print(f'Заметка с id={nid} удалена!')

    print()  # разделитель

def show_note_find():
    print()
    print("Поиск заметки")
    print("-------------")
    nid = input('Введите id искомой заметки: ')
    if not nid.isdigit():
        print('Введенное значение id не является числом. Поиск заметки прерван!')
        return
    status, data = mdl.json_load_from_file()  # загружаем данные из json-файла
    if status == False:
        print(f'ошибка чтения json-файла')

    is_finded = False
    for item in data['note']:
        if str(item['id']) == nid:
            print('Найденная заметка')
            print_tbl([item])       #item помещаем в список, чтобы for смог его обработать
    if not is_finded:
        print(f'Заметка с id={nid} не найдена')
    print()  # разделитель


def show_note_filt_head():
    print()
    print("Фильтрация заметок по заголовку")
    print("-------------")
    str_filter = input('Введите текст фильтра: ')

    status, data = mdl.json_load_from_file()  # загружаем данные из json-файла
    if status == False:
        print(f'ошибка чтения json-файла')

    # убираем в словаре неподходящие записи
    res_list = []
    for i in range(len(data['note'])):
        if (str_filter.upper() in str(data['note'][i]['header']).upper()):
            res_list.append(data['note'][i])

    # Выходим записи, отвечающие критерию
    print('Заметки отфильтрованные по заголовку')
    print_tbl(res_list)
    print()  # разделитель

def show_note_filt_text():
    print()
    print("Фильтрация заметок по тексту")
    print("-------------")
    str_filter = input('Введите текст фильтра: ')

    status, data = mdl.json_load_from_file()  # загружаем данные из json-файла
    if status == False:
        print(f'ошибка чтения json-файла')

    # убираем в словаре неподходящие записи
    res_list = []
    for i in range(len(data['note'])):
        if (str_filter.upper() in str(data['note'][i]['text']).upper()):
            res_list.append(data['note'][i])

    # Выходим записи, отвечающие критерию
    print('Заметки отфильтрованные по тексту')
    print_tbl(res_list)
    print()  # разделитель

def show_note_filt_date():
    print()
    print("Фильтрация заметок по дате создания")
    print("-------------")
    filt_oper = input('Введите:\n1 - ранее указанной даты,\n2 - позднее указанной даты\n')
    filt_date = input('Введите дату фильтрации: ')
    dateFormatter = "%d.%m.%y %H:%M"
    try:
        filt_date_obj = datetime.strptime(filt_date,dateFormatter)
    except Exception as e:
        print(f'Введите дату в формате {dateFormatter}. Например: 28.02.23 1:05')
        return False, ''


    status, data = mdl.json_load_from_file()  # загружаем данные из json-файла
    if status == False:
        print(f'ошибка чтения json-файла')

    # помещаем в результирующий словарь подходящие записи
    res_list = []

    for i in range(len(data['note'])):
        if filt_oper == '1':
            if datetime.strptime(data['note'][i]['created'],dateFormatter) \
                    <= datetime.strptime(filt_date,dateFormatter):
                res_list.append(data['note'][i])
        if filt_oper == '2':
            if datetime.strptime(data['note'][i]['created'],dateFormatter) \
                    >=\
                    datetime.strptime(filt_date,dateFormatter):
                res_list.append(data['note'][i])

    # Выходим записи, отвечающие критерию
    print('Заметки отфильтрованные по тексту')
    print_tbl(res_list)
    print()  # разделитель

def print_tbl(data):
    # ширина столбцов
    lid = 5
    lheader = 20
    lcreated = 16
    ltext = 80
    lrow = lid + lheader + lcreated + ltext + 8     # общая длина строки

    # шапка таблицы
    print(lrow*'-')
    print('|' +
          "| ".join(
              ['id'.center(lid, ' '),
               'header'.center(lheader, ' '),
               'created'.center(lcreated, ' '),
               'text'.center(ltext, ' ')]) +
          '|')
    print(lrow * '-')

    #таблица
    for item in data:
        print('|' +
              "| ".join(
                  [str(item['id']).center(lid, ' '),
                   item['header'].ljust(lheader, ' '),
                   str(item['created']).center(lcreated, ' '),
                   item['text'].ljust(ltext, ' ')]) +
              '|')
    print(lrow * '-')   #футер таблицы