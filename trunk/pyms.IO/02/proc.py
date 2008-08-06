"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation

# path to ANDI-MS data file
andi_file = "/home/current/proj/PyMS/pyms-data/0510_217.CDF"

# get the intensity matrix and save to a file
data = ChemStation(andi_file)

# print the name of the ANDI-MS file
print "ANDI-MS data filename:", data.get_filename()

# get TIC
tic = data.get_tic()

# get the first ion chromatogram
ic = data.get_ic_at_index(1)
# get the ion chromatogram for m/z = 73
ic = data.get_ic_at_mass(73)

# some tests on ion chromatogram objects
print "'tic' is a TIC", tic.is_tic()
print "'ic' is a TIC:",ic.is_tic()

# save TIC to a file
ic.write("output/tic.dat")

# get the entire intensity matrix
im = data.get_intensity_matrix()

print "Dimensions of the intensity matrix are:",len(im),"x",len(im[0])

# save the intensity matrix  to a file
save_data("output/im.dat", im)

# Export the entire data as CSV. This will create
# data.im.csv, data.mz.csv, and data.rt.csv where
# these are the intensity matrix, retention time
# vector, and m/z vector in the CSV format
data.export_csv("output/data")

