'''
Print a given variable along with it's symbolic name

>>> var = 10
>>> printf(var)
var: 10

Written by Steven Kneiser
'''

import inspect
import os
import re
import readline
import sys

def printf(x):
	current_line = inspect.currentframe().f_back.f_lineno
	filename = os.path.abspath(sys.argv[0]) #__file__)
	#print('==> ' + str(current_line))
	#print('==> ' + str(filename))

	# Detect if user is using an interactive shell
	if os.isatty(sys.stdout.fileno()):
		first_line = readline.get_current_history_length()
		readline.get_history_item(first_line + 0) #TODO: find current_line
		print() #TODO
		return

	with open(filename, 'r') as source:
		for n, line in enumerate(source, start=1):
			if n == current_line:
				#print('==> ' + str(line))

				mo = __import__('re').search(r'printf\s*\(\s*([_a-zA-Z][_a-zA-Z0-9]*)\s*\)', line)
				if mo is not None:
					print('{}: {}'.format(mo.group(1), x))
				'''
				else:
					print('Error: Steven\'s regex is broken')
				'''

				break

		else:
			print('Error: symbol not found')


if __name__ == '__main__':
	test_variable = 'value1 is alright'
	printf(test_variable)

