"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader
from pyms.GCMS.Function import build_intensity_matrix, build_intensity_matrix_i
from pyms.GCMS.IO.Function import export_csv, export_leco_csv
from pyms.Utils.IO import save_data

# read the raw data as a GCMS_data object
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)

# IntensityMatrix
# must build intensity matrix before accessing any intensity matrix methods.

# default, float masses with interval (bin size) of one from min mass
print "default intensity matrix, bin size = 1"
im = build_intensity_matrix(data)

print "size of intensity matrix (#scans, #bins):", im.get_size()

print "start mass:", im.get_min_mass()
print "end mass:", im.get_max_mass()

index = im.get_index_of_mass(73.3)
print "the index of the nearest mass to 73.3m/z is:", index
print "the nearest mass to 73.3m/z is:", im.get_mass_at_index(index)
print

# bin size of 0.5, eg. for double charge ions
print "intensity matrix, bin size = 0.5"
im = build_intensity_matrix(data, 0.5)

print "size of intensity matrix (#scans, #bins):", im.get_size()

print "start mass:", im.get_min_mass()
print "end mass:", im.get_max_mass()

index = im.get_index_of_mass(73.3)
print "the index of the nearest mass to 73.3m/z is:", index
print "the nearest mass to 73.3m/z is:", im.get_mass_at_index(index)
print

# integer intensity matrix, integer masses, in one unit steps
print "intensity matrix with integer mass and bin size = 1"
im = build_intensity_matrix_i(data)

print "size of intensity matrix (#scans, #bins):", im.get_size()

print "start mass:", im.get_min_mass()
print "end mass:", im.get_max_mass()

index = im.get_index_of_mass(73.3)
print "the index of the nearest mass to 73.3m/z is:", index
print "the nearest mass to 73.3m/z is:", im.get_mass_at_index(index)
print


masses = im.get_mass_list()


# TIC and SIC

# TIC from raw data
tic = data.get_tic()
# save TIC to a file
tic.write("output/tic.dat",minutes=True)

# get the first ion chromatogram of the IntensityMatrix
ic = im.get_ic_at_index(0)
ic.write("output/ic_index_1.dat",minutes=True)
# get the ion chromatogram for m/z = 73
ic = im.get_ic_at_mass(73)
ic.write("output/ic_mass_73.dat",minutes=True)

# some tests on ion chromatogram objects
print "'tic' is a TIC:", tic.is_tic()
print "'ic' is a TIC:", ic.is_tic()
print

# Data saving

# save the intensity matrix values to a file
mat = im.get_matrix_list()
print "saving intensity matrix intensity values..."
save_data("output/im.dat", mat)

# Export the entire IntensityMatrix as CSV. This will create
# data.im.csv, data.mz.csv, and data.rt.csv where
# these are the intensity matrix, retention time
# vector, and m/z vector in the CSV format
print "exporting intensity matrix data..."
export_csv("output/data", im)

# Export the entire IntensityMatrix as LECO CSV. This is
# useful for import into AnalyzerPro
print "exporting intensity matrix data to LECO CSV format..."
export_leco_csv("output/data_leco.csv", im)
