"""proc.py
"""

import sys
sys.path.append("/x/archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Utils.IO import save_data
from pyms.IO.Function import export_csv, export_leco_csv

# read the raw data
andi_file = "/x/archive/proj/PyMS/data/a0806_140.CDF"
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
print "'tic' is a TIC:", tic.is_tic()
print "'ic' is a TIC:", ic.is_tic()

# save ion chromatograms to a file
tic.write("output/tic.dat",minutes=True)
ic.write("output/ic.dat",minutes=True)

# get the entire intensity matrix
im = data.get_intensity_matrix()

print "Dimensions of the intensity matrix are:",len(im),"x",len(im[0])

# save the intensity matrix  to a file
save_data("output/im.dat", im)

# Export the entire data as CSV. This will create
# data.im.csv, data.mz.csv, and data.rt.csv where
# these are the intensity matrix, retention time
# vector, and m/z vector in the CSV format
export_csv(data, "output/data")

# Export the entire data set as LECO CSV. This is
# useful for import into AnalyzerPro
export_leco_csv(data, "output/data_leco.csv")

