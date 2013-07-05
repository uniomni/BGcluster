"""Configure cluster with host names, IP addresses etc
"""

head_node = 'tambora'
node_names = [head_node]
number_of_processors_per_node = 4  # Cores
node_info = {}
node_info[head_node] = '10.1.1.2'
for i in range(1, 11):
    hostname = 'node%i' % i
    ip_address = '10.1.1.%i' % (10 + i)

    node_names.append(hostname)
    node_info[hostname] = ip_address

