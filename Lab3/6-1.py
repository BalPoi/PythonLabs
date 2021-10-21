with open('ospf.txt', 'r') as ospf:
    for line in ospf:
        l = line.split()
        dict = {
                "Protocol": "OSPF",
                "Prefix": l[1],
                "AD/Metric": l[2][1:-1],
                "Next-Hop": l[4][:-1],
                "Last update": l[5][:-1],
                "Outbound Inteface": l[6]
        }

        for key, value in dict.items():
            print("{0}: {1}".format(key, value), end=' ')
        print()

