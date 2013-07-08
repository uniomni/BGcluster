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
import time
import getpass
import subprocess


def run_remote(username, host, password, 
               directory=None, 
               command=None,
               timeout=None,
               verbose=True, 
               debug=True):
    """Run command on remote host as sudo

    Args
    
    username: user id under which to run. Must have sudo access.
    host: hostname or ip address of remote host
    directory: directory in which to run the command. If None cd to ~
    command: unix command to run. Defaults to 'whoami@hostname' (for testing).
    timeout: Optional timeout in seconds. Default None which means command can run indefinitely.
             If timeout is None run_remote will return immediately letting 
             the command run in the background.
             If timeout is specified, run_remote will wait until command has finished or 
             timeout has been reached in which case an exception is raised.
    verbose: If True print some diagnostics to console
    debug:   If True print the result of stderr and stdout from the command to the console. 
             As a side effect, run_remote will block until command has finished if debug is True.
    """

    if command is None:
        # Default command for diagnostic purposes
        command = 'printf "`whoami`@`hostname`\n"'

    if directory is None:
        directory = '~'

    command_sanitized = command.replace(' ', '_').replace('`', '').replace('\n', '')
    logfile = '/var/tmp/last_remote_exec_%s_%s.log' % (username, command_sanitized)

    if verbose:
        print ('Running command "%s" on %s in directory %s. '
               'See logfile %s for details.' % (command, host, 
                                                directory, logfile))
    p = subprocess.Popen(['ssh', '-t', '-t', '%s@%s' % (username, host),
                          'cd %s; sudo %s > %s' % (directory, command, logfile)],
                         stdin=subprocess.PIPE, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)


    # Write password to process.
    # Use variable either from first time input or file
    p.stdin.write('%s\n' % password)

    password_mask = '*' * len(password)  # Used to replace the real password in stdout echo

    if timeout is not None:
        try:
            timeout = int(timeout)
        except:
            msg = ('Timeout %s could not be cast as an integer. '
                   'Timeout should specify a number of seconds.' % timeout)
            RuntimeError(msg)

        if not timeout > 0:
            msg = ('Timeout should be a positive number of seconds. ' 
                   'I got %i' % timeout)
            RuntimeError(msg)

        t0 = time.time()

        t = time.time() - t0
        while p.poll() is None and t < timeout:
             print 'waiting...', t
             time.sleep(1)
             t = time.time() - t0
        print 'done'     
             
        if t >= timeout:
            p.kill()  # Kill the remote process
            msg = ('Command %s timed out after %i seconds and was killed.\n'
                   'stdout: %s' 
                   'stderr: %s' 
                   % (command, timeout, 
                      p.stdout.read().replace(password, password_mask),  # Suppress password echo
                      p.stderr.read()))
            raise Exception(msg)
        
        if p.returncode != 0:
            msg = ('Command %s returned with return code %i.\n'
                   'stdout: %s' 
                   'stderr: %s' 
                   % (command, p.returncode, 
                      p.stdout.read(), p.stderr.read()))
            raise Exception(msg)


        print 'Command %s returned normally after %i seconds' % (command, t)
        print 'stdout: %s' % p.stdout.read().replace(password, password_mask)  # Suppress password echo
        print 'stderr: %s' % p.stderr.read()
        
        
    # FIXME (Ole): I think if we don't print these, commands will be issued without 
    # waiting for completion. This is great for speed, but perhaps we might get 
    # issues with apt-get on the same host being locked.
    if debug:
        print 'stdout: "%s"' % p.stdout.read().replace(password, password_mask)  # Suppress password echo
        print 'stderr: "%s"' % p.stderr.read()
    

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
    #for host in ['node1', 'node2']:
    for host in ['node2']:

        run_remote(username, host, password, directory=cwd, command=command, debug=False, 
                   timeout=5) 

