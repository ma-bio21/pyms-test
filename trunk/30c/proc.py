"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader
from pyms.GCMS.Function import build_intensity_matrix_i

# read the raw data as a GCMS_data object
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)

# IntensityMatrix
# must build intensity matrix before accessing any intensity matrix methods.

# integer intensity matrix, integer masses, in one unit steps
print "intensity matrix with integer mass and bin interval = 1, "\
    "using default boundary -0.3, +0.7"
im = build_intensity_matrix_i(data)

print " -> size of intensity matrix (#scans, #bins):", im.get_size()

print " -> start mass:", im.get_min_mass()
print " -> end mass:", im.get_max_mass()

index = im.get_index_of_mass(73.3)

print " -> the index of the nearest mass to 73.3 m/z is:", index
print " -> the nearest mass to 73.3 m/z is:", im.get_mass_at_index(index)

