import os
import re
pattern = re.compile("(.*.pyc)|(^\..*)")
for i in os.listdir(os.getcwd()):
	if i != '__init__.py' and not pattern.match(i):
		print 'importing ' + i
		execfile(i)