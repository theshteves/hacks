#!/usr/bin/env python3
'''
Kill python before 'try...finally'

Written by Steven Kneiser
'''
import os
import signal
import subprocess

try:
	# Execute 'ps -A' in bash to print all processes
	shell = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = shell.communicate()

	# Kill all python-related processes by PID
	pids = [str(process, 'utf-8').split()[0] for process in out.splitlines() if b'python' in process]
	for pid in pids:
		os.kill(int(pid), signal.SIGKILL)

finally:
	print('...finally executed.')
