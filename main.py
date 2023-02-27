import datetime
import json

import view

import model_json as mdl


# текущая позиция в меню. Нужно для запоминая текущего положения
cur_menu_pos = []

#Работа с меню
view.show_menu_header()   #показать главное меню в начале
while True:
    ch = ''
    match cur_menu_pos:
        # [] - означает отобразить главное меню
        case []:
            ch = view.show_main_menu()

        # Выбор действия после выбора меню первого уровня 1, 2, 3, 4
        case (['1']):
            view.show_notes_table()
            cur_menu_pos = []
            ch = view.show_main_menu()
        case (['5']):
            view.show_end_program()
            break

        case(['1', '3']):    #Показать весь список, Найти заметку
            ch = view.show_selected_note_menu()



        #case (['1', '6'] | ['2', '6'] | ['3', '6'] | ['4', '6']):
            # Выбор - Назад, возврат в главное меню
        case _:
            #заглушка, для сброса выбора пунктов меню на главное,
            # для тех вариантов для которых нет обработчиков. А также для недопустимых вариантов
            print(f'Отсутствует обработчик для пункта меню: {cur_menu_pos}. Выберите значение из списка.')
            cur_menu_pos = []
        #добавляем выбранный пункт меню в конец текущей позиции меню
    if ch != '':
        cur_menu_pos.append(ch)