# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def parse_cdp_neighbors(command_output):
    """
  Функция обрабатывает вывод команды show cdp neighbors.
  command_output - параметр, принимающий, в качестве аргумент вывод команды show cdp neighbors одной строкой.
  Возвращает словарь, который описывает соединения между устройствами.
    """
    dict_cdp_intf = {}
    command_output = command_output.split("\n")
    for line in command_output:
        amt = len(line.split())
        if line and not (amt == 0 or "Capability" in line or "Switch" in line):
            if "show cdp neighbors" in line:
                main_device = line.replace(">"," ").split()[0]
            else:
                line = line.split()
                local_intf = line[1] + line[2]
                device_id = line[0]
                port_id = line[-2] + line[-1]
                dict_cdp_intf[main_device, local_intf] = (device_id, port_id)
    return dict_cdp_intf


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
