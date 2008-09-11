"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.MSlib.NIST.Class import NIST_library

# the NIST library file
nist_file = "/home/current/proj/PyMS/pyms-data/NIST_sample.lib"

# load the NIST library
nist_lib = NIST_library(nist_file)

# print compounds and their mass spectra
for compound in nist_lib.compounds:
    print "Compound '%s' has '%d' mass peaks" % (compound.name, compound.num_peaks)
    print "Mass spectrum list:\n\t",  compound.mass_spectrum
    print "Mass list:\n\t",  compound.mass_list

