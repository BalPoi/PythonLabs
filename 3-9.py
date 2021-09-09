str = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
#str = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

a = 10

print(len(str) - 1 - str[::-1].index(a))
