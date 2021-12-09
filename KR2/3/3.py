"""
3.Дан файл со списком слов. Разработайте алгоритм, создающий максимально возможный прямоугольник из букв так, 
чтобы каждая строка и каждый столбец образовывали слово (при чтении слева направо и сверху вниз). 
Слова могут выбираться в любом порядке, строки должны быть одинаковой длины, столбцы - одинаковой высоты.
"""

import re

words = []
f = open("input.txt", "r")
words = re.findall(r"[a-zA-Zа-бА-Б]+", f.read())
# print(words)

# numL = []
# numW = []
a = {}
for word in words:
    wordlen = len(word)
    if wordlen in a.keys():
        a[wordlen][0] += 1
        a[wordlen][1].append(word)
    else:
        a[wordlen] = [1, [word]]
# print(a)

edges = []

# print(sorted(list(a.keys()), reverse=True))

for key in sorted(list(a.keys()), reverse=True):
    if a[key][0] >= 4 and len(edges) == 0:
        edges += a[key][1][0:4]
    elif a[key][0] >= 4 and len(edges) == 2:
        edges += a[key][1][0:2]
    elif a[key][0] >= 2 and len(edges) == 0:
        edges += a[key][1][0:2]
    elif a[key][0] >= 2 and len(edges) == 2:
        edges += a[key][1][0:2]
print(edges)

print(edges[0])
for l1, l2 in zip(edges[2], edges[3]):
    print(l1, " "*(len(edges[0])-4), l2)
print(edges[1])