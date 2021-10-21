ip = input('Введите IP в виде 10.0.1.1: ')
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
