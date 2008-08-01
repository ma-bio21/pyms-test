"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation

andi_file = "/home/current/proj/PyMS/pyms-data/0510_217.CDF"

data = ChemStation(andi_file)

# print the name of the ANDI-MS file
print data.get_filename()

# get the first ion chromatogram in the file
ic = data.get_ic_at_index(1)
print ic.is_tic()

# get TIC
tic = data.get_tic()
print tic.is_tic()

# get the ion chromatogram for m/z = 73
ic = data.get_ic_at_mass(73)
print ic.is_tic()

# get the entire intensity matrix
im = data.get_intensity_matrix()
print len(im)
print len(im[0])

