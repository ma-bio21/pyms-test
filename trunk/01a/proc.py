"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.IO.ANDI.Class import Xcalibur
from pyms.Utils.IO import save_data

# path to ANDI-MS data file
andi_file = "/x/proj.archive/proj/PyMS/data/121107B_10.CDF"

# get the intensity matrix and save to a file
andi_data = Xcalibur(andi_file)

# print the name of the ANDI-MS file
print "ANDI-MS data filename:", andi_data.get_filename()

# get TIC
tic = andi_data.get_tic()

# get the first ion chromatogram
ic = andi_data.get_ic_at_index(1)
ic.write("output/ic_index_1.dat",minutes=True)
# get the ion chromatogram for m/z = 73
ic = andi_data.get_ic_at_mass(73)
ic.write("output/ic_mass_73.dat",minutes=True)

# some tests on ion chromatogram objects
print "'tic' is a TIC:", tic.is_tic()
print "'ic' is a TIC:",ic.is_tic()

# save ion chromatograms to a file
tic.write("output/tic.dat",minutes=True)

# get the entire intensity matrix
im = andi_data.get_intensity_matrix()

print "Dimensions of the intensity matrix are:",len(im),"x",len(im[0])

# save the intensity matrix  to a file
save_data("output/im.dat", im)

# Export the entire data as CSV. This will create
# andi_data.im.csv, andi_data.mz.csv, and andi_data.rt.csv where
# these are the intensity matrix, retention time
# vector, and m/z vector in the CSV format
andi_data.export_csv("output/data")

