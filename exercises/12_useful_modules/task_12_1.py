# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(ip_list):
    """
    Функция проверяет пингуются ли IP-адреса.
    ip-list - ожидает в качестве аргумента список ip-адресов.
    Взвращает кортеж с двумя списками:
        - список доступных IP-адресов
        - список недоступных IP-адресов
    """
    alive_ip = []
    unreach_ip = []
    for ip in ip_list:
        command = subprocess.run(['ping', '{}'.format(ip)], stdout=subprocess.DEVNULL)
        if command.returncode == 0:
            alive_ip.append(ip)
        else:
            unreach_ip.append(ip)
    ip_tuple = (alive_ip, unreach_ip)
    return ip_tuple

if __name__ == "__main__":
      ip_list = ["10.0.0.0", "255.255.0.1", "8.8.8.8"]
      ip_tuple = ping_ip_addresses(ip_list)
      print(ip_tuple)





