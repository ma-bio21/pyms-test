"""proc.py
"""
import time
import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.JCAMP.Class import MSLib
from pyms.IO.ANDI.Class import ChemStation

ms_lib_file = "mslib.jcamp"
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"


print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file)
print "Loading end at:", time.localtime()

data = ChemStation(andi_file)
mass_list = data.get_mass_list()
im = data.get_intensity_matrix()
im = im[0]

print "Processing start at: ", time.localtime()
name, max = ms_lib.match(mass_list, im)
print name
print max
print "Processing end at: ", time.localtime()