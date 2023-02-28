import json
import model_json as mdl

# Пример работы с json
str_json = """
{
    "note": [
        {
          "id": 1,
          "header": "Работа с JSON",
          "text": "JSON - JavaScript Object Notation. Это распространенный формат обмена данными",
          "created": "15.12.2022"
        },
        {
          "id": 2,
          "header": "Работа с XML",
          "text": "XML - Extended Markup Language. Это один из самых популярных форматов передачи данных",
          "created": "10.01.2023"
        }
    ]
}
"""

# загружает данные формата json из строки в структуру данных типа Словарь Dict - notesDct
notesDct = json.loads(str_json)

# Записываем словарь в файл json
mdl.json_write_to_file(notesDct)

data2 = []
status, data2 = mdl.json_load_from_file()

print(type(data2))
print(data2)
