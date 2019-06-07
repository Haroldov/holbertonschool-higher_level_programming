#!/usr/bin/python3
import signal
import subprocess
process = subprocess.Popen("./101-fake_gen2.py | ./101-stats.py",
                           shell=True,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,)   # pass cmd and args to the function
process.send_signal(signal.SIGINT)   # send Ctrl-C signal
stdout, stderr = process.communicate()   # get command output and error
print('\tpass through:', str(stdout))
print('\tstderr:', repr(stderr))
