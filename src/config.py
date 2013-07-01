"""Configure cluster with host names, IP addresses etc
"""

node_names = []
node_info = {}
for i in range(1, 11):
    hostname = 'node%i' % i
    ip_address = '10.1.1.%i' % (10 + i)

    node_names.append(hostname)
    node_info[hostname] = ip_address

print node_names
for node in node_names:
    print node, node_info[node]
