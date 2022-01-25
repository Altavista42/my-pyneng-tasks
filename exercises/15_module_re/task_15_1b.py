# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re

regex_key = re.compile(r'interface (?P<intf>\S+).+ip address \S+', re.DOTALL)
regex_value = re.compile(r'ip address (?P<IP>\S+) (?P<mask>\S+)')

def get_ip_from_cfg(config_file):
    """
    Функция обрабатывает конфигурационный файл и выводит имя интерфейса, IP-адрес, маску.
    config_file - Ожидает в качестве аргумента название конфигурационного файла.
    Возвращает словарь:
    - ключ: имя интерфейса
    - значение: список кортежей с двумя строками:
    - IP-адрес
    - маска
    """
    config_dict = {}
    with open(config_file) as conf:
        config = conf.read().split('!')
        for line in config:
            if regex_key.findall(line) and regex_value.findall(line):
                key = regex_key.findall(line)[0]
                value = regex_value.findall(line)
                config_dict[key] = value
    return config_dict


if __name__ == "__main__":
    print(get_ip_from_cfg("config_r2.txt"))
