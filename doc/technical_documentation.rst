
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

This procedure will allow ssh to access nodes without prompting for passwords. This is essential to scripts or MPI programs making use of nodes. The steps need only to be done once for each user. Assuming all nodes share a common NFS mounted `/home` directory the steps are as follows:

Generate encryption key pairs using the command::

    ssh-keygen

When asked for a passphrase just leave it blank and hit RETURN.
Then publish the public key to all nodes using the commands::

    cd .ssh; cat id_rsa.pub >> authorized_keys

To test that it works do for all nodes::
    ssh <node> whoami


.. note 
if `/home` is not shared publishing the public key has to be done remotely as follows (do this for all nodes)::

    ssh-copy-id <node> ~/.ssh/id_rsa.pub
