"""Execute arbitrary commands across cluster using sudo.

This is intended to allow installation of software packages across the cluster.

Usage:

python exec_cluster.py <command>

Examples:

python exec_cluster.py apt-get install python-numpy
python exec_cluster.py python setup.py install

"""

# Sources:
# http://stackoverflow.com/questions/15166973/sending-a-password-over-ssh-or-scp-with-subprocess-popen
# http://www.unix.com/programming/176212-using-commands-over-ssh-using-sudo.html

import os
import sys
import getpass
import subprocess


def run_remote(username, host, password, directory=None, 
               command=None,
               verbose=True, debug=True):
    """Run command on remote host as sudo

    Args
    
    username: user id under which to run. Must have sudo access.
    host: hostname or ip address of remote host
    directory: directory in which to run the command. If None cd to ~
    command: unix command to run. Defaults to 'whoami' (for testing). 
    """

    if command is None:
        # Default command for diagnostic purposes
        #command = 'echo -n `whoami`; echo -n @; echo `hostname`'
        command = 'echo `whoami`'

    if directory is None:
        directory = '~'

    command_sanitized = command.replace(' ', '_').replace('`','').replace(';', ':')
    logfile = '/var/tmp/last_remote_exec_%s_%s.log' % (username, command_sanitized)

    if verbose:
        print 'Running command "%s" on %s in directory %s. See logfile %s for details.' % (command, host, 
                                                                                           directory, logfile)
    p = subprocess.Popen(['ssh', '-t', '-t', '%s@%s' % (username, host),
                          'cd %s; sudo %s > %s' % (directory, command, logfile)],
                         stdin=subprocess.PIPE, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)


    # Write password to process.
    # Use variable either from first time input or file
    p.stdin.write('%s\n' % password)
    if debug:
        print 'stdout: "%s"' % p.stdout.read()
        print 'stderr: "%s"' % p.stderr.read()
    
    if verbose:
        print


def usage():
    s = 'Usage:\t'
    s += 'python exec_cluster.py <command>'

    return s

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        command = ' '.join(sys.argv[1:])
    else:
        command = None

    # Get sudo password (must be the same on all hosts)
    #username = raw_input('Please enter sudo username (must be the same for all nodes): ')
    #password = getpass.getpass('Please enter sudo password (must be the same for all nodes): ')
    username = 'uniomni'
    password = 'dstat43'

    # Get current working directory
    cwd = os.getcwd()
    
    # Run command remotely for each host
    #for host in ['tambora', 'node1', 'node2']:
    for host in ['node1', 'node2']:
        

        run_remote(username, host, password, directory=cwd, command=None)
