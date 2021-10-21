IP = '192.168.3.1'

IP = IP.split('.')

for item in IP:
    print('{:<10}'.format( int(item) ), end='')

print('')

for item in IP:
    print('{:<10b}'.format( int(item) ), end='')
