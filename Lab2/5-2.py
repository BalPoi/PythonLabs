macs = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
macs_cisco = []

for mac in macs:
    macs_cisco.append('.'.join(mac.split(':')))

print(macs_cisco)
