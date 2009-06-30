"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader
from pyms.GCMS.Function import build_intensity_matrix, build_intensity_matrix_i
from pyms.GCMS.IO.Function import export_csv, export_leco_csv
from pyms.Utils.IO import save_data

from pyms.Peak.Class import Peak
from pyms.Deconvolution.BillerBiemann.Functions import get_maxima_indices, \
    get_maxima_list, get_maxima_matrix, sum_maxima, BillerBiemann, \
    rel_threshold, num_ions_threshold

from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat

# read the raw data as a GCMS_data object
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)

# IntensityMatrix
# must build intensity matrix before accessing any intensity matrix methods.

# default, float masses with interval (bin size) of one from min mass
print "default intensity matrix, bin size = 1"
im = build_intensity_matrix(data)

# get the size of the intensity matrix
n_scan, n_mz = im.get_size()
print " Size of the intensity matrix is (n_scans, n_mz):", n_scan, n_mz

# smooth data
for ii in range(n_mz):
    print "Working on IC#", ii+1
    ic = im.get_ic_at_index(ii)
    ic1 = savitzky_golay(ic)
    ic_smooth = savitzky_golay(ic1)
    ic_base = tophat(ic_smooth, struct="1.5m")
    im.set_ic_at_index(ii, ic_base)

# thresholds
# filter width, maxima in 'points' is apex
points = 9
# minimum number of ions, n
n = 3
# greater than or equal to threshold, t
t = 10000
# percentage ratio of ion intensity to max ion intensity
r = 2

# get the list of Peak objects
pl = BillerBiemann(im, points)
#print "Number of Peaks found:", len(pl)

# trim by relative intensity
apl = rel_threshold(pl, r)

# trim by threshold
bpl = num_ions_threshold(apl, n, t)

# output details of peaks
print "\"rt\",\"TIC\",\"number_ions\",\"sorted_intensities...\""
for p in bpl:
    ms = p.get_mass_spectrum().mass_spec
    l = []
    for i in ms:
        if i > 0:
            l.append(i)
    if len(l) > 0:
        print p.get_rt(), sum(l), len (l), sorted(l)
print
