"""Test that Python can enter password to ssh and sudo command
"""

# Sources:
#http://stackoverflow.com/questions/15166973/sending-a-password-over-ssh-or-scp-with-subprocess-popen
# http://www.unix.com/programming/176212-using-commands-over-ssh-using-sudo.html


import subprocess
p = subprocess.Popen(['ssh', '-t', '-t', 'install@203.189.89.245',
                      'sudo whoami'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)

# Write password to process.
# Use variable either from first time input or file
p.stdin.write('tambora13\n')
print p.stdout.read()

