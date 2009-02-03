"""proc.py
"""
import sys
import time

sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.JCAMP.Class import MSLib

ms_lib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp"

print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file)
print "Loading end at:", time.localtime()

