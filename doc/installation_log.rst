===========================
BG Cluster Installation log
===========================

Installing and configuring head node
====================================


Install of Ubuntu 12.04 (64 bit).
---------------------------------

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

Install fundamental packages.
-----------------------------

* apt-get update
* apt-get install openssh-server
* apt-get nfs-kernel-server
* apt-get nfs-common


Make /home available for NFS mount
----------------------------------
tambora (local IP address): 10.1.1.2
nodes : 10.1.1.11 - 20
#we use node1 (10.1.1.11) for instance

#Setting up tambora (head node):
--------------------------------
#ssh to tambora
#set as root
	sudo -s
#Installing nfs program
	apt-get install nfs-kernel-server portmap
#we wanted to share two directories: /home and /var/nfs.
#Because the /var/nfs/ does not exist, we need created itself
	mkdir /var/nfs/

#we should change the ownership of the directory to the user, nobody and the group, no group. 
#These represent the default user through which clients can access a directory shared through NFS. 
	chown nobody:nogroup /var/nfs
#export the directorie
	nano /etc/exports
#sharing both directories with the node
/home           10.1.1.11(rw,sync,no_root_squash,no_subtree_check)
/var/nfs        10.1.1.11(rw,sync,no_subtree_check)
#command to export both directories
exportfs -a

#Setting up node
----------------
#ssh to node from head node (ssh install@10.1.1.11)

#Install the nfs programs
apt-get install nfs-common portmap

#create the directories that will contain the NFS shared files
mkdir -p /mnt/nfs/home
mkdir -p /mnt/nfs/var/nfs

#mount directories from head node
mount 10.1.1.2:/home /mnt/nfs/home
mount 10.1.1.2:/var/nfs /mnt/nfs/var/nfs

#list the directories
df -h

#mount command to see the entire list of mounted file systems.
mount

#moving /home on node to another directory (e.g /home_old)
rm /home /home_old

#create symlinks from nfs directory to the node new /home
ln -s /mnt/nfs/home /home

#Testing the NFS mount
----------------------
# on the node /home, create new file to test nfs 
nano abc.txt

#if nfs mount successfully setted up, abc.txt should be apper on head node /home

--

/etc/exports stuff

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

Install fundamental packages.
-----------------------------

 * apt-get update
 * apt-get install openssh-server
 * apt-get nfs-common

NFS mount /home to head node
----------------------------


/etc/fstab stuff on the clients


Configure entire cluster through scripts
----------------------------------------

Passwordless ssh
mounting of NAS
