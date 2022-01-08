# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
config_filename = argv[1]

def get_int_vlan_map(config_filename):
    """
    Функция обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:
     - словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа).
     - словарь портов в режиме trunk, где ключи номера портов,а значения список разрешенных VLAN (список чисел).
    """
    dict_access = {}
    dict_trunk = {}
    with open(config_filename) as config:
         new_list = config.read().replace('\n',' ').split('!')
         for line in new_list:
             if 'access' in line:
                 intf_access = line.split()[1]
                 vlan_access = int(line.split()[-3])
                 dict_access[intf_access] = vlan_access
             if 'trunk' in line:
                 intf_trunk = line.split()[1]
                 dict_trunk[intf_trunk] = [int(item) for item in line.replace(' ',',').split(",") if item.isdigit()]
    return dict_access, dict_trunk








