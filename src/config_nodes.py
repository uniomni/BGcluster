"""Configure all clients remotely

It is assumed that nodes have passwordless ssh established and that 
user has sudo privileges.
"""

import os
import getpass
from config import node_names
from exec_remote_sudo import run_remote

# First, we check how many nodes can be pinged and and ssh'd into

# Here are some code snippets testing that nodes can be pinged and ssh'd into.

failed = node_names[2:]
print
for node in node_names:
    if node in failed: continue
    #print 'Trying to contact %s' % node

    # First try using hostname
    s = 'ping -c 1 %s' % node
    s += '> /dev/null'
    err = os.system(s)
    #print 'err', err

    if err == 0:
        print 'PING: Node %s OK' % node
    else:
        print 'PING: Node %s FAILED' % node
        failed.append(node)

print
# Check ssh among those that could be pinged
for node in node_names:
    if node in failed: continue

    # First try using hostname
    s = 'ssh %s "hostname"' % node
    s += ' 1> /dev/null'
    s += ' 2> /dev/null'
    err = os.system(s)

    if err == 0:
        print 'SSH: Node %s OK' % node
    else:
        print 'SSH: Node %s FAILED' % node
        failed.append(node)


# Mount all filesystems remotely

# sudo password (must be the same on all hosts)
username = raw_input('Please enter sudo username (must be the same for all nodes): ')
password = getpass.getpass('Please enter sudo password (must be the same for all nodes): ')

for node in node_names:
    if node in failed: 
        continue

    print 'Running mount -a on node %s' % node
    run_remote(username, node, password, directory=None) #, command='mount -a -v')
