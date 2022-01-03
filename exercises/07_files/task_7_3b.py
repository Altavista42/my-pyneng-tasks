# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
num_vlan = int(input("Enter VLAN number: "))
sort_list = []
with open("CAM_table.txt", "r") as cam_table:
    for line in cam_table:
        new_list = line.split()
        list_len = len(new_list)
        if list_len > 2:
            if new_list[0].isdigit() and int(new_list[0]) == num_vlan:
                new_list.remove("DYNAMIC")
                vlan = new_list[0]
                mac = new_list[1]
                port = new_list[2]
                print(f"{vlan:<4}     {mac:<14}      {port:<5}")

