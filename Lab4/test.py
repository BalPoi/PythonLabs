access_mode_template = [        #interface <key>
    "switchport mode access",
    "switchport access vlan",   #<key.value>
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

result = {
    "a": {
        "aa": "aa-text",
        "ab": "ab-text"
    }
}

