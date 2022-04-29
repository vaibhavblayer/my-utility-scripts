#renaming files using python

import os
import itertools


os.chdir('/Users/vaibhavblayer/images')
cwd = os.getcwd()

files = os.listdir()

for file in files:
	x, y = os.path.splitext(file)
	u = x.split('-')
	new_file = u[0] 
	print(u)
#	os.rename(file, new_file)


