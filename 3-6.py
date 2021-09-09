ospf_route = 'O            10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
l = ospf_route.split()
dict = {
        "Protocol": "OSPF",
        "Prefix": l[1],
        "AD/Metric": l[2][1:-1],
        "Next-Hop": l[4][:-1],
        "Last update": l[5][:-1],
        "Outbound Inteface": l[6]
}

for key, value in dict.items():
    print("{0:20}\t{1}".format(key+':',value))
