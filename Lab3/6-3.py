with open('CAM_table.txt', 'r') as mac:
    for i in range(6):
        mac.readline()

    macs = mac.readlines()
    for line in macs:
        params = line.split()
        print("{0}   {1}   {3}".format(*params))
