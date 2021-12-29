# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_list = []
count_iter = 0
count_broad = 0
count_unas = 0
while True:
	ip = input("Введите IP-адрес в формате \"10.10.10.10\": ")
	ip_check = ip.split(".")
	ip_len = len(ip_check)
	ip_correct = True

	if ip_len == 4:
		for value in ip_check:
			if not (value.isdigit() == True and int(value) in range(0, 256)):
				ip_correct = False
				break
	else:
		ip_correct = False
	if ip_correct == True:
		break
	print("Неправильный IP-адрес")

for string in ip_check:
	ip_list.append(int(string))
for num in ip_list:
	if num in range(1, 224):
		print("unicast")
		break
	elif num in range(224, 240):
		print("multicast")
		break
	elif num == 255:
		count_broad += 1
		if count_broad == 4:
			print("local broadcast")
			break
	elif num == 0:
		count_unas += 1
		if count_unas == 4:
			print("unassigned")
			break
	else:
		print("unused")
		break

