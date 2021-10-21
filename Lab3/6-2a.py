#import sys
#f = sys.argv[1]
ignore = ['duplex', 'alias', 'Current configuration']

f = input("Введите название файла: ")
with open(f, 'r') as config:
    for line in config:
        if (line[0] != '!' and not bool(set(ignore) & set(line.split()))):
            print(line.rstrip())
        
