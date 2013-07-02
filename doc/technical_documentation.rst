===========================
BG Cluster Installation log
===========================

This document outlines the technical steps taken to build the Ubuntu 12.04 Beowulf cluster at Badan Geologi in July 2013. Although derived from this particular installation, most of the information is generic and could be useful for other clusters.

The cluster consists of one headnode and 10 compute nodes with a 3 common NAS units. As the compute nodes boot from local disks the initial steps are necessarily manual. However, beyond the basic installation configuration management is scripted where possible.

The source code and technical documentation for this project are available at https://bitbucket.org/ismailsunni/bgcluster


Installing and configuring head node
====================================


Install of Ubuntu 12.04 (64 bit)
--------------------------------

:hostname: tambora
:username: install

configure network manually as below


Network configuration of headnode
---------------------------------


 * apt-get purge network-manager
 * sudo ifup eth0 eth1
 * modify /etc/network/interfaces as follows::

    auto lo
    iface lo inet loopback

    auto eth0 eth1

    iface eth0 inet static
    	address 203.189.89.245
    	netmask 255.255.255.248
    	network 203.189.89.240
    	broadcast 203.189.89.248
    	gateway 203.189.89.241
    	dns-nameservers 203.189.88.10
    	dns-search esdm.go.id

    iface eth1 inet static
    	address 10.1.1.2
            netmask 255.255.255.0
            network 10.1.1.0
            broadcast 10.1.1.255
            gateway 10.1.1.1
            dns-nameservers 10.1.1.1


 * sudo /etc/init.d/networking restart

Install fundamental packages
----------------------------

* apt-get update
* apt-get install openssh-server
* apt-get nfs-kernel-server
* apt-get nfs-common


Make /home available for NFS mount
----------------------------------
tambora (local IP address): 10.1.1.2
nodes : 10.1.1.11 - 20

Setting NFS on tambora (head node):
-------------------------------
 * Login to tambora::
     ssh install@tambora.vsi.esdm.go.id

 * Change to root::
     sudo -s

 * Install nfs packages::
     apt-get install nfs-kernel-server portmap

 * Make /home available for mounting by editing /etc/exports (using node1 (10.1.1.11) as example::
     /home 10.1.1.11(rw,sync,no_root_squash,no_subtree_check)

 * Export all::
     exportfs -a



Installing and configuring compute nodes
========================================

Install of Ubuntu 12.04 (64 bit)
--------------------------------

:hostname: node<1-10>
:username: install

configure network manually as below


Network configuration of compute nodes
--------------------------------------

 * apt-get purge network-manager
 * sudo ifup eth0
 * modify /etc/network/interfaces as follows::

    auto lo
    iface lo inet loopback

    auto eth0

    iface eth0 inet static
    	address 10.1.1.<11-20>
            netmask 255.255.255.0
            network 10.1.1.0
            broadcast 10.1.1.255
            gateway 10.1.1.1
            dns-nameservers 10.1.1.1


 * sudo /etc/init.d/networking restart

Install fundamental packages
----------------------------

 * apt-get update
 * apt-get install openssh-server
 * apt-get install nfs-common portmap


Setting up NFS mount of /home on nodes
--------------------------------------

 * ssh to node from head node::
    ssh install@10.1.1.11

 * Create the directories that will contain the NFS shared files::
    mkdir -p /mnt/nfs/home

 * Add to /etc/fstab::
    10.1.1.2:/home /mnt/nfs/home nfs defaults 1 1

 * list the mounted filesystems::
    df -h

 * Change to root::
     sudo -s

 * Move /home on node to another directory (e.g /home_old)::
    mv /home /home_old

 * Create symlinks from nfs directory to the node new /home::
    ln -s /mnt/nfs/home /home

Testing the NFS mount
---------------------
 * on the node /home, create new file to test nfs
    touch abc.txt

 * if nfs mounted successfully, abc.txt should be appear on head node /home with the correct user and group ids.

Passwordless ssh
----------------
TBA

Mounting of NAS
---------------
TBA

Configure entire cluster through scripts
----------------------------------------

# Need section about getting scripts and docs from bitbucket!

 * Run server configuration (e.g. writing /etc/hosts)::
   sudo python configure_server.py
 * 

