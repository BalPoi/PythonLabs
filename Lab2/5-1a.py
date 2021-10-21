ip = input('Введите IP в виде 10.0.1.1: ')

try:
    1 / (len(ip.split('.')) == 4)
    for byte in ip.split('.'):
       1 / (0 <= int(byte) <= 255)
except ZeroDivisionError:
    print('Incorrect IPv4 address')
else:
    firstByte = ip.split('.')[0]

    if (1 <= int(firstByte)<= 223):
        print('unicast')
    elif (224 <= int(firstByte) <= 239):
        print('multicast')
    elif (ip == '255.255.255.255'):
        print('local broadcast')
    elif (ip == '0.0.0.0'):
        print('unassigned')
    else:
        print('unused')
