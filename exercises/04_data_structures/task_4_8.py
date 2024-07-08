# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ip = "192.168.3.1"
ip_split = ip.split('.')

okt1 = (int(ip_split[0]))
okt2 = (int(ip_split[1]))
okt3 = (int(ip_split[2]))
okt4 = (int(ip_split[3]))
#okt1, okt2, okt3, okt4 = int(ip.split('.'))
print(f'''
    {okt1:<8}  {okt2:<8}  {okt3:<8}  {okt4:<8}
    {okt1:08b}  {okt2:08b}  {okt3:08b}  {okt4:08b}''')
