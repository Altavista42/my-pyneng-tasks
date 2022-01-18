# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate

def print_ip_table(reach_ip, unreach_ip):
    """
    Функция отображает таблицу доступных и недоступных IP-адресов.
    reach_ip - ожидает в качестве аргумента список доступных IP-адресов.
    unreach_ip - ожидает в качетсве аргумента список недостпных IP-адресов.
    Возвращает на стандартный поток вывода таблицу вида:
    
    Reachable    Unreachable
    -----------  -------------
    10.1.1.1     10.1.1.7
    10.1.1.2     10.1.1.8
		 10.1.1.9
    """
    main_dict = {}
    main_dict["Reachable"] = reach_ip
    main_dict["Unreachable"] = unreach_ip
    return print(tabulate(main_dict, headers = "keys"))

if __name__  == "__main__":
    reach_ip = ["10.1.1.1", "10.1.1.2"]
    unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
    print (print_ip_table(reach_ip, unreach_ip))