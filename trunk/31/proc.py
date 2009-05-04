"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader
from pyms.Utils.IO import save_data

# read the raw data as a GCMS_data object
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)

im = build_intensity_matrix_i(data)

print "size of intensity matrix (#scans, #bins):", im.get_size()

masses = im.get_mass_list()

print "start mass:", min(masses)
print "end mass:", max(masses)

im.reduce_mass_spectra()

# save the intensity matrix values to a file
mat = im.get_matrix_list()
print "saving the intensity matrix ..."
save_data("output/im1.dat", mat)

