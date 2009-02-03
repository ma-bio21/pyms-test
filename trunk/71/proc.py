"""proc.py
"""
import time
import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.JCAMP.Class import MSLib
from pyms.IO.ANDI.Class import ChemStation

ms_lib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp"
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"

print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file)
print "Loading end at:", time.localtime()

