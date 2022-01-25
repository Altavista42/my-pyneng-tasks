# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re


def convert_ios_nat_to_asa(config_file, NAT_ASA_file):
	"""
	Функция конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.
	config_file - ожидает в качестве аргумента имя файла, в котором находится правила NAT Cisco IO
	NAT_ASA_file - ожидает в качестве аргумента имя файла, в который надо записать полученные правила NAT для AS
	Ничего не возвращает.
	"""
	regex = re.compile(r'tcp (?P<IP>\S+) (?P<local_port>\d+)(?:\s+\S+){2} (?P<out_port>\d+)')
	ASA_template = """
object network LOCAL_{}
 host {}
 nat (inside,outside) static interface service tcp {} {}
	"""
	with open(config_file) as config, open(NAT_ASA_file, 'w') as dest:
		for line in regex.finditer(config.read()):
			IP = line.group('IP')
			local_port = line.group('local_port')
			out_port = line.group('out_port')
			dest.write((ASA_template.format(IP, IP, local_port, out_port).rstrip()))

if __name__ == '__main__':
	convert_ios_nat_to_asa('cisco_nat_config.txt','ASA_NAT.txt')

