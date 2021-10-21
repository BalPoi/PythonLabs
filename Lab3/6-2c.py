#import sys
#f = sys.argv[1]
ignore = ['duplex', 'alias', 'Current configuration']

f = input("Введите название input: ")
o = input("Введите название output: ")
out = open(o, 'w')
with open(f, 'r') as config:
    for line in config:
        if (not bool(set(ignore) & set(line.split()))):
            out.write(line) 
