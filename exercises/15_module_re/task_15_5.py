# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re

def generate_description_from_cdp(config_file):
    """
    Функция обрабатывает вывод команды show cdp neighbors и генерирует
    на основании вывода команды описание для интерфейсов.
    config_file - ожидает в качестве аргумента имя файла с выводом команды show cdp neighbors
    Возвращает словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса.
    """
    regex = re.compile(r'(?P<device>\S+)\s+(?P<local_intf>\w+\s+\d+/\d+).+?(?P<port_id>\w+\s+\d+/\d+)')
    value_template = 'description Connected to {} port {}'
    conf_dict = {}
    with open(config_file) as config:
        for line in regex.finditer(config.read()):
            device, local_intf, port_id = line.group('device','local_intf','port_id')
            conf_dict[local_intf] = value_template.format(device, port_id)
    return conf_dict


if __name__ == '__main__':
    print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))


