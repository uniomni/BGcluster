1 July 2013
-----------

 * Created planning board for project notes: https://realtimeboard.com/app/5110424/BG-Cluster
 * Created repository for source code and documentation: https://bitbucket.org/ismailsunni/bgcluster
 * Decided on names and ip address space for cluster: https://bitbucket.org/ismailsunni/bgcluster/src/27fb7fe5ad74f76cbdf7ea529e8d365e8c33d7e7/src/config.py?at=master
 * Made proof of concept that system commands can be issued remotely by scripts: https://bitbucket.org/ismailsunni/bgcluster/src/27fb7fe5ad74f76cbdf7ea529e8d365e8c33d7e7/src/ssh_test.py?at=master
 * Reinstalled head node and documented steps.
 * Reinstalled node1 and node2
 * Looked into using LDAP for distributed user authentication.
 * Looked into ways of managing distributed installation including apt-move and puppet
 * NFS mounted /home from node1 to head node and documented process: https://bitbucket.org/ismailsunni/bgcluster/src/48a6c0c42e02fc7ac0f61ac0cc6d9ac197a0eefb/doc/technical_documentation.rst?at=master
 * Started technical documentation (as per link above).

2 July 2013
-----------

 * Created script to write /etc/hosts file: https://bitbucket.org/ismailsunni/bgcluster/src/c0353be09dc6c872c5f18c7b596b0439742fe012/src/config_server.py?at=master
 * Investigated puppet but looks like it only really works for .deb packages. In addition it kept causing nodes to hang.
 * Verified installation of python-FALL3D, pypar, openmpi and their dependencies in preparation for installation when tambora is read.
 * Installed Synology NAS server.
 * Made first cut of a remote sudo install script and verified it could install .deb packages and Python setup.py: https://bitbucket.org/ismailsunni/bgcluster/src/791bc6f2f810e0902a0fc2518153cdd7cd1dc8f3/src/exec_remote_sudo.py?at=master
 * Kept documentation up to date.


Setbacks
........
 * Lost internet access to tambora for more than 2 hours
 * Synology server was not installed and installation disks have gone missing
 * Techical problems with the AusAID system in Jakarta required Rangga to divert his attention away for the cluster (It turned out that all accounts at AIFDR had expired 2nd July).
 * Issue at BNPB with real time earthquake impact server distracted the team in Bandung.
 * The 2 Buffalo NAS servers do not have NFS server installed (perhaps only designed for Windows?)


Next steps
----------

 * Mount the NAS on head and compute nodes. Update technical docs (Rangga and Cipta).
 * Build node2, node3, node4 (Cipta)
 * Update config_server to create mount points generate fstab with mounts on nodes (Rangga)
 * Continue with LDAP (Rangga - Perkerjaan Rumah)
 * Start scripting (config_nodes.py) installation of packages and configuration on nodes (Ismail and Ole)
 * Trying to configure MPI and run a parallel program
 * Network timings (down the track)
 * Keep docs up to date
 * Start creating user documentation for users like Anjar (Cipta)
 * Start creating sysadm docs (e.g. how to install packages and create users).

3 July 2013
-----------

 * Built node3 and node4, mounted their /home to head node. We now have 4 running nodes.
 * Scripted configuration of /etc/fstab on head node including the synology NAS
 * Mounted synology NAS to running nodes
 * Got remote installation script into a workable shape with error messages and timeout option.
 * Installed basic deb packages using remote install script
 * Installed pypar using setup.py with remote install script. Verified tests pass on head and compute nodes
 * Installed Python-FALL3D in /home area
 * Scripted configuration of /etc/mpihosts on head node
 * Configured MPI and verified that pypar examples run and scale across multiple nodes (Ole and Ismail)

Setbacks
........
 * Had to move repository due to limitations on bitbucket

Next steps
..........

 * Run Python-FALL3D using real data and verify that results are as expected (Cipta)
 * Run Python-FALL3D in parallel and verify that it scales (Cipta and Adele Crozier-Bear)
 * Continue with LDAP (Rangga - Perkerjaan Rumah for Monday)
 * Network timings (down the track)

