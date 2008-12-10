"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.MSlib.NIST.Class import NIST_library

# the NIST library file
nist_file = "/x/proj.archive/proj/PyMS/data/pyms-data/NIST_sample.lib"

# load the NIST library
nist_lib = NIST_library(nist_file)

# print compounds and their mass spectra
for compound in nist_lib.compounds:
    print "Compound '%s' has '%d' mass peaks" % \
            (compound.name, compound.num_peaks)
    print "  m/z (first 10):\n\t", compound.mass_list[:10]
    print "  mass spectrum (first 10):\n\t", compound.mass_spectrum[:10]

