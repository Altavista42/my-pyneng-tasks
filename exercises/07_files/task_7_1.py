# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ospf_template = """
{:<18}    {:<18}
{:<18}    {:<18}
{:<18}    {:<18}
{:<18}    {:<18}
{:<18}    {:<18}
"""
with open("ospf.txt", "r") as ospf:
    for line in ospf:
        new_list = line.replace(",", "").split()
        print(ospf_template.format("Prefix", new_list[1], "AD/Metric", new_list[2][1:7], "Next-Hop", new_list[4],
                                   "Last update", new_list[5], "Outbound Interface", new_list[6]))