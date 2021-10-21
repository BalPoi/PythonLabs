command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

command1 = set(command1.split()[4].split(','))
command2 = set(command2.split()[4].split(','))

print(list(command1.intersection(command2)))
