# -*- coding: utf-8 -*-

'''
Задание 9.3a

Переделать функцию parse_cfg из задания 9.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import sys
import re

def a():
  fileName = sys.argv[1]
  # regex = sys.argv[2]
  regex = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
  f = open(fileName, "r")
  config = f.read()
  # print(config)
  matches = re.findall(regex, config)
  for index, item in enumerate(matches):
    # print(index, item)
    matches[index] = tuple(item.split())

  print(matches)

a()
