# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re


def parse_sh_cdp_neighbors(config):
	"""
	Функция обрабатывает вывод команды show cdp neighbors.
	config - ожидает в качестве аргумента вывод команды одной строкой.
	Функция возвращает словарь, который описывает соединения между устройствами.
	"""
	device = re.compile(r'(?P<main>\S+)>')
	neighbor = re.compile(r'(?P<ID>\S+)\s+(?P<local>\S+\s+\d+/\d+).+?(?P<port_id>\w+\s+\d+/\d+)')
	conf_dict = {}
	for line in device.finditer(config):
		main_id = line.group('main')
		conf_dict[main_id] = {}
	for line in neighbor.finditer(config):
		ID, local, port_id = line.group('ID', 'local', 'port_id')
		conf_dict[main_id][local] = {}
		conf_dict[main_id][local][ID] = port_id
	return conf_dict





if __name__=="__main__":
	with open('sh_cdp_n_sw1.txt') as f:
		print(parse_sh_cdp_neighbors(f.read()))

