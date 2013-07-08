
Individual task
===============

Mount local directory to the NAS
--------------------------------

Tambora itself has only a few hundred GB of disk space whereas the NAS has over 7TB. It is therefore important to use this space rather than having files in individual users's home directories. 
One mechanism for this is to create symbolic links (or shortcuts) from local directories to directories on the NAS.

If for example user uniomni wants to have a local directory called tephra mapped to to the NAS, the steps are

 1 Create the tephra dir on the NAS if it doesn't already exist, e.g::

   mkdir /mnt/nfs/modeling_area/tephra

 2 Link the local directory to the NAS::

   ln -s /mnt/nfs/modeling_area/tephra ~/tephra



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
