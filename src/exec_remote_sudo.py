"""Execute arbitrary commands across cluster using sudo.

This is intended to allow installation of software packages across the cluster.

Usage:

python exec_cluster.py <command>

Examples:

python exec_cluster.py apt-get install python-numpy
python exec_cluster.py python setup.py install

"""

# Sources:
#http://stackoverflow.com/questions/15166973/sending-a-password-over-ssh-or-scp-with-subprocess-popen
# http://www.unix.com/programming/176212-using-commands-over-ssh-using-sudo.html

import os
import sys
import getpass
import subprocess


def run_remote(username, host, password, directory=None, command='whoami'):
    """Run command on remote host as sudo

    Args
    
    username: user id under which to run. Must have sudo access.
    host: hostname or ip address of remote host
    directory: directory in which to run the command. If None cd to ~
    command: unix command to run. Default to 'whoami' (for testing). 
    """
    logfile = '/var/tmp/last_remote_exec_%s.log' % (command.replace(' ', '_'))

    if directory is None:
        directory = '~'

    p = subprocess.Popen(['ssh', '-t', '-t', '%s@%s' % (username, host),
                          'cd %s; sudo %s > %s' % (directory, command, logfile)],
                         stdin=subprocess.PIPE)

    # Write password to process.
    # Use variable either from first time input or file
    p.stdin.write('%s\n' % password) 

def usage():
    s = 'Usage:\t'
    s += 'python exec_cluster.py <command>'

    return s

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print usage()
        sys.exit() 
    else:
        command = ' '.join(sys.argv[1:])

    # Get sudo password (must be the same on all hosts)
    username = raw_input('Please enter sudo username (must be the same for all nodes): ')
    password = getpass.getpass('Please enter sudo password (must be the same for all nodes): ')

    # Get current working directory
    cwd = os.getcwd()
    
    # Run command remotely for each host
    for host in ['tambora', 'node1']:
        print 'Running command "%s" on %s in directory %s. See logfile %s for details.' % (command, host, cwd, logfile)

        run_remote(username, host, password, cwd, command)
