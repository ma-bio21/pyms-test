"""proc.py
"""
import sys
import time

sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.JCAMP.Class import MSLib
from pyms.libMS.JCAMP.Class import MatchedObj
from pyms.libMS.JCAMP.IO import ms_lib_match
from pyms.IO.ANDI.Class import ChemStation

ms_lib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp"
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"

print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file)
print "Loading end at:", time.localtime()

# load the GC-MS data
data = ChemStation(andi_file)

# get the m/z list for 'data'
mass_list = data.get_mass_list()

# search the library for the scan 536

# get the scan 536
s = data.get_scan_at_index(536)

# match against the library
result = ms_lib_match(ms_lib, mass_list, s)
matched_obj = MatchedObj(result)

# print results
print "Best hit is:", matched_obj.compound
print "Best hit score:", matched_obj.score
print "Best hit mass spectrum:", matched_obj.mass_spec

