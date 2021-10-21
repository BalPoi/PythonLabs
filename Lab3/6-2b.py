#import sys
#f = sys.argv[1]
ignore = ['duplex', 'alias', 'Current configuration']

f = input("Введите название файла: ")
out = open("config_sw1_cleared.txt", 'w')
with open(f, 'r') as config:
    for line in config:
        if (not bool(set(ignore) & set(line.split()))):
            out.write(line) 
