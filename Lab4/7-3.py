def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, "r") as config:
        for line in config:
            if line.startswith("interface ") and line[10] in ['F','G']:
                interface = line[10:-1]
            elif line.startswith(" switchport access vlan "):
                vlan = int(line[24:-1])
                access_dict[interface]=vlan
            elif line.startswith(" switchport trunk allowed vlan "):
                vlans = line[31:-1].split(',')
                trunk_dict[interface]=vlans

    return (access_dict, trunk_dict)


print(get_int_vlan_map("config_sw1.txt"))