access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}


def generate_access_config(intf_vlan_mapping, access_template):
    result = []
    for interface, vlan in intf_vlan_mapping.items():
        # print(key, value)
        result.append("interface " + interface)
        for command in access_template:
            if command[-4:] == "vlan":
                result.append(command + " " + str(vlan))
            else:
                result.append(command)
    return result

print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config_2, access_mode_template))