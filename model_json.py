import json
import os.path

f_name = "notes.json"

#json-строка пустой БД. для случая когда изначально БД нет, либо файл БД утерян
empty_json_str = """
{
    "note": []
}
"""

def json_load_from_file():
    global f_name

    #если json-файл отсутствует, то предлагает создать пустой, по шаблону
    if not os.path.exists(f_name):
        # предлагаем создать новую пустую БД json-файл
        ch = input(f'Файл БД {f_name} отсуствует. Создать новый json-файл - ? y/n')
        if ch.upper() == "Y":
            try:
                #считываем json-строку в словарь словарей data
                data = json.loads(empty_json_str)
                #далее пишем словарь словарей в json-файл на диск. По сути создаем заново БД
                with open(f_name, "w") as write_file:
                    json.dump(data, write_file, indent=2)
            except Exception as e:
                return False, f'Ошибка создания файла {f_name}. {e}'

    #если файл существует, пытаемся считать его
    try:
        with open(f_name, "r") as file:
            data = json.load(file)
    except Exception as e:
        return False, f'Ошибка чтения из файла {f_name}. {e}'
    return True, data


def json_write_to_file(data):
    # функция добавляет список словарей dat в json-файл f_name
    # параметры:
    # f_name - название файла
    # data - словарь данных для записи его в формате json
    # Результат: либо True  и ''
    # либо False и сообщение об ошибке
    global f_name

    try:
        with open(f_name, "w") as write_file:
            json.dump(data, write_file, indent=2)
    except Exception as e:
        return False, f'Ошибка записи в файл {f_name}. {e}'
    return True, ''