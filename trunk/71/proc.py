"""proc.py
"""
import sys
import time

sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.Class import MSLib

ms_lib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp"

print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file, format="JCAMP")
print "Loading end at:", time.localtime()

# print first 10 records from the library
ms_lib.printl(begin=1,end=10)

