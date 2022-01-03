# -*- coding: utf-8 -*
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
source = argv[1]
dest = argv[2]
list_result = []
ignore = ["duplex", "alias", "configuration"]
with open(source) as config:
    for line in config:
        if not (line.startswith("!")):
            new_list = line.split()
            set_intersect = set(new_list).intersection(set(ignore))
            if not set_intersect:
                list_result.append(line)
    with open(dest, "w") as result:
        result.writelines(list_result)
