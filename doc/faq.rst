Frequently Asked Questions
==========================



What if apt-get fails on a node?
--------------------------------

Running config_nodes.py may sometimes show a message about apt-get being locked on a particular node::

    Running command "apt-get install -y openmpi-bin libopenmpi-dev python-dev python-numpy python-numpy python-scientific gfortran python-gdal gdal-bin libnetcdf-dev" on node7 in directory ~. See logfile /var/tmp/last_remote_exec_install_apt-get_install_-y_openmpi-bin_libopenmpi-dev_python-dev_python-numpy_python-numpy_python-scientific_gfortran_python-gdal_gdal-bin_libnetcdf-dev.log for details.
    stdout: "*********
    [sudo] password for install: 
    E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)
    E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?
    "
    stderr: "Connection to node7 closed.
    "   

This may mean that apt-get is already running on the node or maybe never was terminated. To trouble shoot, login in to the node in question and run::

    ps aux | grep apt-get

If apt-get is running, you can kill it using its process ID (sudo kill -9 PID) and then make sure it will work::

    apt-get clean
    apt-get update

Then try to run config_nodes.py again
