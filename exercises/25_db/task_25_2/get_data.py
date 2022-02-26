# -*- coding: utf-8 -*-
import sqlite3
from sys import argv
from tabulate import tabulate


def check_arg(db_filename, users_arg_list, allow_arg_list):
    '''
    Функция выполняет проверку корректности аргументов, введенных пользователем.
    users_arg_list - ожидает список, состоящий из аргументов, введенных пользователем;
    allow_arg_list - ожидает список допустимых значений паррметров;
    db_filename - ожидает имя файла, содержащего базу данных
    В случае успешной проверки возвращает информацию из базы данных в ответ на требуемый запрос.
    Если проверка не была пройдена - просит проверить корректность ввода и повторить попытку.
    '''
    if len(users_arg_list) == 0:
        full_db(db_filename)
    elif len(users_arg_list) == 2:
        key, value = users_arg_list[1:]
        if key not in allow_arg_list:
            print('Данный параметр не поддерживается.'
                  'Допустимые значения парметров {}'.format(allow_arg_list))
        users_query_db(db_filename, key, value)
    else:
        print('Пожалуйста, введите два или ноль аргументов')


def full_db(db_filename):
    '''
    Функция выводит всё содержимое таблицы dhcp
    db_filename - ожидает имя базы данных, содержащей табоицу dhcp
    Возвращает информацию из таблицы dhcp
    '''
    print('В таблице dhcp такие записи: ')
    print('-' * 40)
    conn = sqlite3.connect(db_filename)
    result = conn.execute('select * from dhcp')
    print(tabulate(result))
    conn.close()


def users_query_db(db_filename, users_key, users_value):
    '''
    Функция обрабатывает параметр и его значение, введенного пользователем.
    db_filename - ожидает имя файла, содержащего базу данных;
    users_key - ожидает имя параметра, запрошиваемого пользователем;
    users_value - ожидает значение соответствующего параметра.
    Возвращает информацию из базы данных, соответствующую запросу.
    '''
    conn = sqlite3.connect(db_filename)
    query = 'select * from dhcp where {} = ?'.format(users_key)
    result = conn.execute(query, (users_value,))
    print('\nИнформация об устройствах с такими параметрами: ', users_key, users_value)
    print('-' * 40)
    print(tabulate(result))
    conn.close()


if __name__ == '__main__':
    db_filename = 'dhcp_snooping.db'
    allow_arg_list = ['mac', 'ip', 'vlan', 'interface', 'switch']
    users_arg_list = argv[1:]
    check_arg(db_filename, users_arg_list, allow_arg_list)


