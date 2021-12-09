"""
1.В файле записаны координаты пар точек так, что в каждой строке записаны координаты нескольких точек. 
Каждая координата отделена от другой пробелом. Например, строка вида 5 8 -8 3 означает, что координаты первой точки (5;8), 
второй - (-8;3). Во второй файл требуется построчно записать расстояние между парами точек из первого файла.
"""
lis = []
with open("input.txt", 'r') as inputfile:
    for line in inputfile:
        for a in line.split():
            lis.append(int(a))
print(lis)

f = open("output1.txt", "w")
for i in range(0, int(len(lis)/2)):
    f.write("({};{})\n".format(lis[i*2], lis[i*2+1]))
f.close()

f = open("output2.txt", "w")
for i in range(0, int(len(lis)/4)):
    x1 = lis[i*2]
    y1 = lis[i*2+1]
    x2 = lis[(i+1)*2]
    y2 = lis[(i+1)*2+1]
    f.write("{}\n".format(((x2-x1)**2 + (y2-y1)**2)**0.5))
f.close()