"""
2.Из текстового файла 
    - удалить все слова, содержащие от трех до пяти символов, 
    - но при этом из каждой строки должно быть удалено только четное количество таких слов

Текст из input.txt:
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
Aenean sagittis dui non urna efficitur,
vel auctor velit semper.
Integer dolor sapien,
pellentesque id ante sed,
lacinia convallis odio.
Mauris facilisis dolor sed felis volutpat vestibulum.
Nullam eu elit nunc.
Mauris vitae hendrerit nisi.
Proin vehicula sapien et augue elementum, et ornare tortor interdum.
Aliquam erat volutpat. Nunc non pharetra elit.
Quisque odio est, sollicitudin id posuere et,
gravida eu est. Integer et pretium dui. Ut lorem urna,
fermentum eget ornare sit amet, varius vel felis.
"""

import re


words = []
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        words.append(re.findall(r"[a-zA-Zа-бА-Б\n]+", line))
print(words)


numSuitableWords = []
wordsToDelete = []
for i in range(0, len(words)):
    # print(words[i])
    count = 0
    wordsToDelete.append([])
    for word in words[i]:
        if 3 <= len(word) < 5:
            count += 1
            wordsToDelete[i].append(word)
    numSuitableWords.append(count)

# for a, b in zip(numSuitableWords, wordsToDelete):
#     print(f'{a}: {b}')

result = ""
for i in range(0, len(words)):  #for line
    for j in range(0, len(wordsToDelete[i]) if numSuitableWords[i] % 2 == 0 else len(wordsToDelete[i])-1):   #for words
        words[i].remove(wordsToDelete[i][j])
    result += " ".join(words[i])
# print(result)

f = open("input.txt", "w")
f.write(result)