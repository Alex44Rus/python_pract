"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml


def write_dict_to_yaml(dict, file):
    with open(file, 'w') as f_n:
        yaml.dump(dict, f_n, sort_keys=False, default_flow_style=False,
                  allow_unicode=True)

    with open(file) as f_n:
        f_n_content = yaml.safe_load(f_n)

    print(f_n_content == dict)


my_spares = {
    '100€': ['Miles', 'Lynx', 'Stellox'],
    '200€': 146,
    '300€': {
        'brand': ['Miles', 'Lynx', 'Stellox'],
        'warranty': 12,
    }
}

write_dict_to_yaml(my_spares, 'file.yaml')
