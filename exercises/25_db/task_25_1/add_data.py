# -*- coding: utf-8 -*-
import glob
import os
import sqlite3
import re
import yaml


def add_data(db, query, data):
    """
    Функция вполняет добавление данных в БД. Выполняет проверку на наличие ошибок.
    db - ожидает имя базы данных;
    query - ожидает запрос;
    data - данные, которые должны быть внесены  в БД
    """
    conn = sqlite3.connect(db)
    for row in data:
        try:
            with conn:
                conn.execute(query, row)
        except sqlite3.IntegrityError as error:
            print('При добавлении данных: ', row, 'Возникла ошибка: ', error)
    conn.close()


def parse_dhcp(conf_file):
    """
    Функция выполняет парсинг вывода команды sh ip dhcp snooping binding
    conf_file - ожидает имя файла, содержащего вывод команды sh ip dhcp snooping binding
    """
    regex = re.compile(r'(?P<mac>\S+)\s+(?P<IP>\S+)\s+\d+.+?(?P<vlan>\d+)\s+(?P<intf>\S+)')
    sw = re.search("(\w+)_dhcp_snooping.txt", conf_file).group(1)
    with open(conf_file) as conf:
        match = regex.search(conf.read())
        dhcp_data = [match.groups() + (sw,) for match in regex.finditer(conf.read())]
    return dhcp_data


def fill_table_dhcp(db_name, files_dhcp):
    """
    Функция добвляет информацию на основании вывода sh ip dhcp snooping binding в таблицу dhcp БД
    db_name - имя базы данных
    files_dhcp - ожидает список имен файлов, содержащих вывод команды sh ip dhcp snooping
    """
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
        return
    print('Добавляю данные в таблицу dhcp...')
    query_dhcp = 'insert into dhcp values (?, ?, ?, ?, ?)'
    result_dhcp = []
    for next_file in files_dhcp:
        result_dhcp.extend(parse_dhcp(next_file))
    add_data(db_name, query_dhcp, result_dhcp)


def fill_table_switches(db_name, yaml_file):
    """
    Функция добавляет в таблицу switches данные о коммутаторе.
    db_name - имя базы данных;
    yaml_file - ожидает имя файла в формате yaml,
    содержащий данные о наименовании коммутатора и его месторасположении;
    """
    db_exist = os.path.exists(db_name)
    if not db_exist:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
        return
    print('Добавляю данные в таблицу switches...')
    query_yaml = 'insert into switches values (?, ?)'
    with open(yaml_file) as yml_source:
        sw_info = yaml.safe_load(yml_source)
    sw_result = list(sw_info['switches'].items())
    add_data(db_name, query_yaml, sw_result)


if __name__ == '__main__':
    dhcp_snoop = glob.glob("sw*_dhcp_snooping.txt")
    db_filename = 'dhcp_snooping.db'
    fill_table_dhcp(db_filename, dhcp_snoop)
    fill_table_switches(db_filename, 'switches.yml')


