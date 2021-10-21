#import sys
#f = sys.argv[1]
f = input("Введите название файла: ")
with open(f, 'r') as config:
    for line in config:
        if (line[0] != '!'):
            print(line.rstrip())
config.close()
