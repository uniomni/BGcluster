1 July 2013
-----------

Achievements
............

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

Achievements
............

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
..........

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

Achievements
............

 * Built node3 and node4, mounted their /home to head node. We now have 4 running nodes.
 * Scripted configuration of /etc/fstab on head node including the synology NAS
 * Mounted synology NAS to running nodes
 * Got remote installation script into a workable shape with error messages and timeout option.
 * Installed basic deb packages using remote install script
 * Installed pypar using setup.py with remote install script. Verified tests pass on head and compute nodes
 * Installed Python-FALL3D in /home area
 * Scripted configuration of /etc/mpihosts on head node
 * Configured MPI and verified that pypar examples run and scale across multiple nodes (Ole and Ismail)
 * Ran network timing code (C code from pypar) and verified 100 Mbit network.

Setbacks
........
 * Had to move repository due to limitations on bitbucket
 * Lost contact to all nodes about 7pm - appeared to be hanging. All came back 15 minutes later and we verified pypar parallel example ran perfectly on 4 nodes (16 processes). No idea what had happened.

Next steps
..........

 * Run Python-FALL3D using real data and verify that results are as expected (Cipta)
 * Run Python-FALL3D in parallel and verify that it scales (Cipta and Adele Crozier-Bear)
 * Continue with LDAP (Rangga - Perkerjaan Rumah for Monday): https://help.ubuntu.com/lts/serverguide/openldap-server.html

    
Next Steps:
...........

 * Continue OpenLDAP config: Access Control and TLS (rangga)

4 July 2013
-----------

Achievements
............

 * Installed OpenLDAP Server
 * Anjar verified that PythonFALL3D works sequentially using the merapi and Guntur validations examples.
 * Investigated problem with nodes hanging - looks like lingering puppet-agent might have been the issue (/var/log/syslog)
 *

Next Steps:
...........

 * Build remaining nodes and run install script (Cipta). Verify documentation is OK (Cipta). Verify parallel examples work across all nodes (40 processes) (Ismail).
 * Port node_activity script to monitor cluster from and identify where there is spare capacity (Ismail).
 * Run Python-FALL3D using forecasting data (Anjar)
 * Run Python-FALL3D in parallel and verify that it scales (Anjar, Ismail and Adele Crozier-Bear)
 * Continue with LDAP (Rangga - Perkerjaan Rumah for Monday): https://help.ubuntu.com/lts/serverguide/openldap-server.html


5 July 2013
-----------

Achievements
............

 * Ran probabilistic ashfall model on 8 cores and verified results.
 * Fine tuned configure_nodes to not show password in cleartext
 * First cut of node_activity working
 * Built node5, .. ?

Setbacks
........

 * Nodes hung spontaneously again today - just after lunch.


8 July 2013
-----------

Plan
....

 * Rangga to concentrate on LDAP
 * Ismail and Amalfi to install EQRM
 * Ryan to come to Bandung on Wednesday (10th) to install ANUGA
 * Cipta and Ole to finish building the rest of the nodes

Achievements
............

 * Built all remaining nodes and verified that test_cluster.py passed for all 10.
 * Verified that MPI example ran sucessfully across all 40 processing elements (10 nodes with 4 cores each).


Setbacks
........

 * An electricity outage on the weekend had taken the nodes down. System was rebooted this morning and appeared to work for a little while. However, around 9:45 contact was lost spontaneously to all of them and their screens reported kernel panic. Screenshots and contents of dmesg and syslog was added to the repository. Upon rebooting, nodes could be contacted again but NAS mount was not working causing df -h and ls to hang. At 11:15 Cipta isolated a problem with the network switch and restarted it. Subsequently, cluster appeared to work normally again.
 * At 15:15 - without any thing being run - 5 nodes dropped spontaneously with node1 to node4 in kernel panic and node7 just hanging. Ut was quite hot in the server room. The kernel panic error was the same again about "BUG: unable to handle kernel paging request at <hex address>" on node1 to node4. The hanging node, node7, presented with a blank graphical screen. When dropping to terminal (Alt F1) it allowed username and password to be entered, the hung. Rebooting all nodes allowed all tests to pass again. Logfiles showed "Jul  8 15:14:31 node7 kernel: [12008.162766] nfs: server 10.1.1.2 not responding, still trying" and node showed that it had drifted to a time in the future 22:29:10.
 * Replaced network switch as problems re-emerged and persisted throughout afternoon. When all nodes were switched off it was still showing much traffic so something wasn't right. New network switch appeared be more swift but after 10 minutes we lost the abilty to ping tambora let alone log in. Network diagnostics indicated this might be a problem external to the cluster and Cipta decided to investigate. We'll all reconvene in the morning and focus on getting Tambora back on the net. 

9 July 2013
-----------

Plan
....

 * Understand problem with hanging nodes - then get on with it!


Achievements
............

 * Disconnected switch from router to isolate from external network (11am). Rangga noticed that the router was serving 3 IP addressed on one port that connected to the cluster switch. Maybe this was the problem.
 * Modified network configuration on head node (tambora) to only use eth0 with local IP address
 * Ran a large range of tests including big MPI runs (10k x 10k matrices with cyclic, blockwise and dynamic load balancing) for a few hours. No problems experienced as of 13:00.
 * At 13:15 fan stopped in node9 and warning sounds were emitted from the UPS due to heat generated by cluster. We turned all nodes off to cool down. Also noted that all units were powered from one source so think that cluster is probably undersupplied with electricity.
 * 14:00 - started switch, NAS, tambora, node1 and node2 until aircon and power has been sorted
 * Installed EQRM and ANUGA and verified test suites pass
 * Amalfi confirmed EQRM runs
 * Rangga and Cipta reconfigured the network, verified tests worked much faster than before and documented the configuration. No cases of kernel panic.
 * Rangga got LDAP to work.


10 July 2013
------------

Status
......

 * Cluster switched off and removed from server room while aircon and electricity is being properly installed.
 * Apparently 3 nodes (node3, node4, and node9) were down because their UPS was damaged maybe due to underpowering. They were plugged to the same UPS which probably ran out off power somehow.
 * All tests, network and parallel examples were working mell last night on the 7 remaining nodes.

Plan
....

 * Update docs
 * Get Ryan up to speed and get access to repository
 * When (if) cluster is back online verify that everything still works and establish status

Status 14:45
............

Cluster came back online with node1 and node2 up and running shortly after 2pm. We proceeded to run tests and found they ran correctly but sluggish as previously. Succesfully ran MPI examples and network timing with perfect results. After about 15 minutes both nodes crashed. Cipta observed a UPS beeping in the server room (connected to the headnode and NAS so doesn't explain node1 and node2 crashing).

Restarted cluster with node1, node2, node3, node4, node5 and node6 running, but Synology NAS switched off.
Reran cluster test (OK) and flogged the 6 nodes with MPI programs for about 30 minutes. No problems encountered.

15:30 - Additionally started node7, node8, node9 and node10. Ran MPI examples on all nodes (network on, NAS off). No problems after 20 minutes except node10 lost power due to faulty power cable.

15:50 - Restarted MPI dynamic LB example on all 10 nodes.

16:00 - Headnode down due to UPS failing (power was supplied but UPS stopped causing head node to switch off).

16:14 - Connected to head node again and could ping all compute nodes. However none were reachable through ssh. One of the nodes showed the familiar kernel panic screen with the error message about not being able to handle kernel paging request. 

16:19 - Restarted MPI dynamic LB example on all 10 nodes (NAS off, network on) to see if problem can be reproduced (and not interrupted by power outages).

16:56 - MPI job completed successfully. All nodes still up. 

17:00 - Switched NAS back on and verified cluster tests passing.
17:15 - Started MPI example again on all nodes.


