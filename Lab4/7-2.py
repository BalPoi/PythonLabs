trunk_dict = {
    'FastEthernet0/1':[10,20],
    'FastEthernet0/2':[11,30],
    'FastEthernet0/4':[17]
    }

def generate_trunk_config(trunk):
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
        ]
    result = []
    for interface, vlans in trunk.items():
        result.append("interface " + interface)
        for command in trunk_template:
            if command[-4:] == "vlan":
                result.append(command + " " + ",".join([str(vlan) for vlan in vlans]))
            else:
                result.append(command)

    return result

print(generate_trunk_config(trunk_dict))