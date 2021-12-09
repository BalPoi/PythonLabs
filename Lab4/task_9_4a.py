# -*- coding: utf-8 -*-
"""
Задание 7.4a

Задача такая же, как и задании 7.4. Проверить работу функции надо на примере
файла config_r1.txt
Обратите внимание на конфигурационный файл. В нем есть разделы с большей
вложенностью, например, разделы:
interface Ethernet0/3.100
router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам. Она должна быть универсальной,
и сработать, если это будут другие разделы.

Задания:
    - если уровня 2, то команды верхнего уровня будут ключами словаря, а команды
подуровней - списками;
    - если уровня 3, то самый вложенный должен быть списком, а остальные -
словарями.
На примере interface Ethernet0/3.100
{
    "interface Ethernet0/3.100": {
        "encapsulation dot1Q 100": [],
        "xconnect 10.2.2.2 12100 encapsulation mpls": [
            "backup peer 10.4.4.4 14100",
            "backup delay 1 1",
        ],
    }
}
"""

ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status


def leftSpaceCounter(string):
    """
    IN: String
    OUT: Number of spaces from left to first non-space
    Exemple: " text" -> 1; "text" -> 0
    """
    count_space = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count_space += 1
        else:
            return count_space


def convert_config_to_dict(config_filename):
    config_dict = {}
    path = []
    with open(config_filename, "r") as config:
        for line in config:
            if not ignore_command(line, ignore) and line[0] != "\n" and line[0] != "!":
                num_space = leftSpaceCounter(line)
                if num_space == 0:
                    config_dict[line.strip()] = []
                    path = path[:0]
                    path.append(line.strip())
                elif num_space == 1:
                    config_dict[path[0]].append(line.strip())
                    path = path[:1]
                    path.append(line.strip())
                elif num_space == 2:
                    if type(config_dict[path[0]]) is not dict:
                        config_dict[path[0]] = dict.fromkeys(config_dict[path[0]], [])
                    config_dict[path[0]][path[1]].append(line.strip())
                    path = path[:2]
                    path.append(line.strip())
                # elif num_space == 3:
                #     config_dict[path[0]][path[1]][path[2]].append(line.strip())
                #     path = path[:2]
                #     path.append(line.strip())

                # if line[0] != " ":
                #     prev = line.strip()
                #    config_dict[line.strip()] = []
                # else:
                #    config_dict[prev].append(line.strip())

    return config_dict


print(convert_config_to_dict("config_r1.txt"))
