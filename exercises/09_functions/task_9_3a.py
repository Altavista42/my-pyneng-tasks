# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
config_filename = argv[1]

def get_int_vlan_map(config_filename):
    """
    Функция обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:
     - словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа).
     - словарь портов в режиме trunk, где ключи номера портов,а значения список разрешенных VLAN (список чисел).
     В случае, если access порт находится во VLAN 1 - в словарь портов добавляется строка с указанием интерфейса
     в качестве ключа и в качестве значения указывается цифра 1.
    """
    dict_access = {}
    dict_trunk = {}
    with open(config_filename) as config:
         new_list = config.read().replace('\n',' ').split('!')
         for line in new_list:
             if 'access vlan' in line:
                 intf_access = line.split()[1]
                 vlan_access = int(line.split()[-3])
                 dict_access[intf_access] = vlan_access
             if 'access' in line and 'vlan' not in line:
                 intf_access = line.split()[1]
                 dict_access[intf_access] = 1
             if 'trunk' in line:
                 intf_trunk = line.split()[1]
                 dict_trunk[intf_trunk] = [int(item) for item in line.replace(' ',',').split(",") if item.isdigit()]
    return dict_access, dict_trunk
