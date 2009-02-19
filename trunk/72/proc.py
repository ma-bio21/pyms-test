"""proc.py
"""
import sys
import time

sys.path.append("/home/qiaow/Desktop/pyms-read-only")

from pyms.libMS.JCAMP.Class import MSLib
from pyms.libMS.JCAMP.Class import MatchedObj
from pyms.libMS.JCAMP.Class import MassSpectrum
from pyms.libMS.Function import ms_lib_match
from pyms.IO.ANDI.Class import ChemStation

ms_lib_file = "/home/qiaow/PyMS/pyms-data/NIST08.JCAMP"
andi_file = "/home/qiaow/PyMS/pyms-data/a0806_140.CDF"

# load the GC-MS data
data = ChemStation(andi_file)

print "Loading start at:", time.localtime()
ms_lib = MSLib(ms_lib_file)
print "Loading end at:", time.localtime()

# search the library for the scan 536

# get the scan 536
ms = MassSpectrum(data, 536)

# match against the library
result = ms_lib_match(ms_lib, ms)
matched_obj = MatchedObj(result)

# print results
print "Best hit is:", matched_obj.compound
print "Best hit score:", matched_obj.score
print "Best hit mass spectrum:", matched_obj.mass_spec