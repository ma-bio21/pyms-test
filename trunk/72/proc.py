"""proc.py
"""
import sys
import time

sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.JCAMP.Class import MSLib
from pyms.libMS.JCAMP.Function import ms_lib_match 
from pyms.IO.ANDI.Class import ChemStation

ms_lib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp"
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"

print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file)
print "Loading end at:", time.localtime()

# load the GC-MS data
data = ChemStation(andi_file)

# prime the library for matching against 'data'
mass_list = data.get_mass_list()
ms_lib.prime_records(mass_list)

#
# scans matching
#

# get the number of scans
N = data.get_scan_size()
# initiate the list of matches
matches = []

for ii in range(N):
    print "Working on scan", ii
    s = data.get_scan_at_index(ii)
    best_match = ms_lib_match(s, ms_lib)
    matches.append(best_match)

