"""Synchronise existing user from head node to compute nodes

It is assumed that
 1. User exists (created e.g. with the adduser command)
 2. The directory /home is shared by headnode and all compute nodes
 3. The user account from which this script is run has sudo access and exists on headnode and all nodes

Algorithm:
   1. Copy the files passwd, group, shadow and gshadow from /etc on head node 
      to temporary directory in /home using sudo
   2. Run remote sudo command on each compute node to copy these four files to /etc on the node.


Usage:
    python synchronise_user_account.py <username>
"""

# This is a fallback only if we can't get LDAP to work properly.
pass
