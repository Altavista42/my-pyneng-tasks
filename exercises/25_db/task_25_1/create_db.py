# -*- coding: utf-8 -*-
import sqlite3
import os

def create_db(db_name, schema):
    db_exists = os.path.exists(db_filename)
    if not db_exists:
        print('Создаю базу данных...')
        with open(schema_filename, 'r') as f:
            schema = f.read()
            conn = sqlite3.connect(db_filename)
            conn.executescript(schema)
            conn.close()
        print('База данных создана')
    else:
        print('База данных существует')


if __name__ == '__main__':
    db_filename = 'dhcp_snooping.db'
    schema_filename = 'dhcp_snooping_schema.sql'
    create_db(db_filename, schema_filename)
