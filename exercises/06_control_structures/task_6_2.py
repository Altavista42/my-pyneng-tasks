# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP-адрес в формате 10.0.0.1: ")
ip_str = ip.split(".")
ip_int = []
count_iter = 0
count_unas = 0
count_broad = 0
for i in ip_str:
	ip_int.append(int(i))

for num in ip_int:
	count_iter += 1
	if num in range(1, 224) and count_iter == 1:
		print("unicast")
		break
	elif num in range(224, 240) and count_iter == 1:
		print("multicast")
		break
	elif num == 255:
		count_broad += 1
		if count_broad == 4 and count_iter == 4:
			print("local broadcast")
			break
	elif num == 0:
		count_unas += 1
		if count_unas == 4 and count_iter == 4:
			print("unassigned")
			break
else:
	print("unused")






