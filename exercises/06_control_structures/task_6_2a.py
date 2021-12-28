# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP-адрес в формате \"10.10.10.10\": ")
ip_check = ip.split(".")
ip_list = []
count_iter = 0
count_broad = 0
count_unas = 0
ip_len = len(ip_check)

for value in ip_check:
    if ip_len == 4 and value.isdigit() == True and int(value) in range(0, 256):
        count_iter += 1
        if count_iter == 4:
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
    else:
        print("Неправильный IP-адрес")
        break

