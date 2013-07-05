===========================
BG Cluster Installation log
===========================

This document outlines the technical steps taken to build the Ubuntu 12.04 Beowulf cluster at Badan Geologi in July 2013. Although derived from this particular installation, most of the information is generic and could be useful for other clusters.

The cluster consists of one headnode and 10 compute nodes with a 3 common NAS units. As the compute nodes boot from local disks the initial steps are necessarily manual. However, beyond the basic installation configuration management is scripted where possible.

The source code and technical documentation for this project are available at https://bitbucket.org/ismailsunni/bgcluster

To login to the cluster as administrator run::

    ssh install@tambora.vsi.esdm.go.id


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
* apt-get install nfs-kernel-server
* apt-get install nfs-common
* apt-get install git


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

Mounting of NAS
---------------
# 3 NAS ( 1 Synology, 2 Buffalo Linkstation)
# Capacity Synology NAS is 10 Terabyte
# Capacities of both Buffalo Linkstation NAS are 4 Terabyte for each NAS
	
	* Set up first NAS with Synology Assistant
	* Configure network:: 

		 IP address 10.1.1.50
		 Netmask 255.255.255.0
		 Gateway 10.1.1.1	

	* Set up user details ::

		username: admin
		password: *********
		NAS name : nas1

	* Installing DSM 4.2 from Resources CD or Synology Download Center http://www.synology.com/support/download.php?lang=enu&b=5%20bays&m=DS1512%2B
	* Create volume 1 with all hard drive using RAID 5, so the capacity will reduce from 10 Terabyte to 7.5 Terabyte
	* Create shared folder (e.g /volume1/modeling)
			
Mount NAS shared folder to headnode (This part has been scripted inside config_server.py)
-----------------------------------
	* Create folder on the headnode to mount NAS's shared folder::

		sudo -s
		mkdir -p /mnt/nfs/modeling_area

	* Edit /etc/fstab, add this following line (10.1.1.50 is IP of NAS)::

		10.1.1.50:/volume1/modeling /mnt/nfs/modeling_area nfs defaults 1 1

	* Then you can run something like the following to see your files on the NAS::

		mount 10.1.1.50:/volume1/modeling /mnt/nfs/modeling_area

	* Type df -h to see list of filesystem

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
 * on the node /home, create new file to test nfs::

    touch abc.txt

 * if nfs mounted successfully, abc.txt should be appear on head node /home with the correct user and group ids.

Create new user (optional)
--------------------------

 * sudo adduser <username>
 * sudo adduser <username> sudo  # If admin access is required

Passwordless ssh
----------------

Create passwordless access for a particular user across cluster 

 * ssh-keygen

If /home is shared through NFS mount across nodes
 * cd .ssh; cat id_rsa.pub >> authorized_keys

If /home is not shared (do this for all nodes)
 * ssh-copy-id <node> ~/.ssh/id_rsa.pub

To test
 * ssh <host> whoami

Configure entire cluster through scripts
----------------------------------------

# Getting scripts and docs from bitbucket:
	
 * Requires Git Client to bitbucket repos
 * Follow the instruction to setup SSH for Git in https://confluence.atlassian.com/display/BITBUCKET/How+to+install+a+public+key+on+your+Bitbucket+account
 * Get the files from the repos::

    git clone git@bitbucket.org:cipta_muhamad_firmansyah/bgcluster.git

 * Run server configuration (e.g. writing /etc/hosts)::

    sudo python config_server.py

 * 


Install OpenLDAP Server
-----------------------
 * Installing OpenLDAP Server:
 
   * Modify /etc/hosts/::
     
      127.0.1.1       tambora.example.com     tambora
     
   * Install OpenLDAP::
   
      sudo apt-get install slapd ldap-utils
   
   * Modifying/Populating your Database:
   
     Create file ~/sandpit/ldap_config_files/add_content.ldif::
     
      dn: ou=Users,dc=example,dc=com
      objectClass: organizationalUnit
      ou: People

      dn: ou=Groups,dc=example,dc=com
      objectClass: organizationalUnit
      ou: Groups

      dn: cn=modelling,ou=Groups,dc=example,dc=com
      objectClass: posixGroup
      cn: modelling
      gidNumber: 5000

      dn: uid=john,ou=Users,dc=example,dc=com
      objectClass: inetOrgPerson
      objectClass: posixAccount
      objectClass: shadowAccount
      uid: john
      sn: Doe
      givenName: John
      cn: John Doe
      displayName: John Doe
      uidNumber: 10000
      gidNumber: 5000
      userPassword: johnldap
      gecos: John Doe
      loginShell: /bin/bash
      homeDirectory: /home/john
   
     Add the content::
     
      ldapadd -x -D cn=admin,dc=example,dc=com -W -f add_content.ldif

   * Logging:
   
     Create file ~/sandpit/ldap_config_files/logging.ldif::
   
      dn: cn=config
      changetype: modify
      add: olcLogLevel
      olcLogLevel: stats
        
     Implement the change::
     
      sudo ldapmodify -Q -Y EXTERNAL -H ldapi:/// -f logging.ldif
