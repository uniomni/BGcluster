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
