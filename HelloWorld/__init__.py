import sys
import os

print("this.__init__.__path__ BEFORE change:",__path__)
dirname = __path__[0]
if sys.platform[0:5]=="linux" :
	__path__.insert(0, os.path.join(dirname,'Linux'))
else:
	__path__.insert(0, os.path.join(dirname,"window"))
print("this.__init__.__path__ AFTER change:",__path__)