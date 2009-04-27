"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader
from pyms.GCMS.Function import build_intensity_matrix, build_intensity_matrix_i
from pyms.GCMS.IO.Function import export_csv, export_leco_csv

# read the raw data and return GCMS_data object
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)

# IntensityMatrix
# must build intensity matrix before accessing any intensity matrix methods.

# default, float masses with interval (bin size) of one from min mass
print "default intensity matrix, bin size = 1"
im = build_intensity_matrix(data)

print "size of intensity matrix (#scans, #bins):", im.get_size()

masses = im.get_mass_list()

print "start mass:", min(masses)
print "end mass:", max(masses)

index = im.get_index_of_mass(73.3)
print "the index of the nearest mass to 73.3m/z is:", index
print "the nearest mass to 73.3m/z is:", masses[index]
print

# bin size of 0.5, eg. for double charge ions
print "intensity matrix, bin size = 0.5"
im = build_intensity_matrix(data, 0.5)

print "size of intensity matrix (#scans, #bins):", im.get_size()

masses = im.get_mass_list()

print "start mass:", min(masses)
print "end mass:", max(masses)

index = im.get_index_of_mass(73.3)
print "the index of the nearest mass to 73.3m/z is:", index
print "the nearest mass to 73.3m/z is:", masses[index]
print

# integer intensity matrix, integer masses, in one unit steps
print "intensity matrix with integer mass and bin size = 1"
im = build_intensity_matrix_i(data)

print "size of intensity matrix (#scans, #bins):", im.get_size()

masses = im.get_mass_list()

print "start mass:", min(masses)
print "end mass:", max(masses)

index = im.get_index_of_mass(73.3)
print "the index of the nearest mass to 73.3m/z is:", index
print "the nearest mass to 73.3m/z is:", masses[index]

# TIC from raw data
tic = gcms_data.get_tic()
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

# Export the entire data as CSV. This will create
# data.im.csv, data.mz.csv, and data.rt.csv where
# these are the intensity matrix, retention time
# vector, and m/z vector in the CSV format
export_csv(data, "output/data")

# Export the entire data set as LECO CSV. This is
# useful for import into AnalyzerPro
export_leco_csv(data, "output/data_leco.csv")
