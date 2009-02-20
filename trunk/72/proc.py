"""proc.py
"""
import sys
import time

sys.path.append("/x/archive/proj/PyMS/")

from pyms.libMS.Class import MSLib
from pyms.libMS.Function import ms_lib_match
from pyms.IO.ANDI.Class import ChemStation
from pyms.IO.Class import MassSpectrum

ms_lib_file = "/x/archive/proj/PyMS/data/mslib.jcamp"
andi_file = "/x/archive/proj/PyMS/data/a0806_140.CDF"

# load the GC-MS data
data = ChemStation(andi_file)

print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file, format="JCAMP")
print "Loading end at:", time.localtime()

# search the library for the best hit to the scan 536

# get the mass spectrum at scan 536
ms = MassSpectrum(data, 536)

# match against the library
best_match = ms_lib_match(ms_lib, ms)

# print results
print "Best hit is:", best_match.id
print "Best hit score:", best_match.score
print "Best hit mass spectrum:", best_match.mass_record

