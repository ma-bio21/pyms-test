"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix, build_intensity_matrix_i
from pyms.GCMS.IO.Function import export_csv, export_leco_csv
from pyms.Utils.IO import save_data

from pyms.Deconvolution.BillerBiemann.Functions import get_maxima_indices, \
    get_maxima_list, get_maxima_matrix, BillerBiemann

# read the raw data as a GCMS_data object
#jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
andi_file = "/x/PyMS/data/gc01_0812_073.cdf"
data = ANDI_reader(andi_file)

# IntensityMatrix
# must build intensity matrix before accessing any intensity matrix methods.

# default, float masses with interval (bin size) of one from min mass
print "default intensity matrix, bin size = 1"
im = build_intensity_matrix(data)

print "size of intensity matrix (#scans, #bins):", im.get_size()

masses = im.get_mass_list()


# TIC and SIC

# TIC from raw data
tic = data.get_tic()
# save TIC to a file
tic.write("output/tic.dat",minutes=True)

index = im.get_index_of_mass(73)
ic = im.get_ic_at_index(index)
ic.write("output/ic_mass_73.dat",minutes=True)

peaks = get_maxima_list(ic)
save_data("output/peaks.csv", peaks)

# Export the entire IntensityMatrix as LECO CSV. This is
# useful for import into AnalyzerPro
print "exporting intensity matrix data to LECO CSV format..."
export_leco_csv("output/data_leco.csv", im)


# get all maxima for all ions
print "finding all maxima"
peaks_matrix = []
for mass in masses:
    ic = im.get_ic_at_mass(mass)
    ia = ic.get_intensity_array()
    peaks_matrix.append(get_maxima_indices(ia))

# count all maxima across all ions
print "creating histogram"
count = []
for index in range(len(ic)):
    num = 0
    for ii in range(len(peaks_matrix)):
        if index in peaks_matrix[ii]:
            num += 1
    count.append(num)

# wrap it up an save
print "saving histogram"
out = []
for index in range(len(ic)):
    rt = ic.get_time_at_index(index)
    out.append([rt, count[index]])
save_data("output/counts.csv", out)

# biller biemann
print "Biller Biemann reconstructed TIC"
bbtic = BillerBiemann(im)
bbtic.write("output/bbtic.csv")
