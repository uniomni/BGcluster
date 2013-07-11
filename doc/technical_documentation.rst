
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


How to see what is running on Tambora
-------------------------------------

To what is running on Tambora and its 10 nodes run::

    python node_activity.py

which is available in `bgcluster/src`

It will take a few minutes to produce the result as it'll run `top` on every node and aggrate the statisitics.

It is often convenient to have this script running and updating automatically. To do this run::

    watch -n 5 python node_activity.py


How to run jobs on Tambora
--------------------------

Firstly, determine which nodes are free running the node_activity.py script described above. Then either run the job sequentially by logging into a node or in parallel using MPI. 

Running sequentially
....................

Login to the desired node (e.g. node5)::

    ssh node5

Then run the job normally, e.g::

    python <script_name>


Running in parallel
...................

To run a job in parallel use `mpirun` e.g. ::

    time mpirun -np 40 -x FALL3DHOME -x PYTHONPATH -hostfile /etc/mpihosts python guntur_multiple_wind.py


For more info about options to mpirun see http://www.open-mpi.org/doc/v1.4/man1/mpirun.1.php


