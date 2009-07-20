"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat
from pyms.Peak.Class import Peak
from pyms.Peak.IO import store_peaks
from pyms.Deconvolution.BillerBiemann.Functions import BillerBiemann, \
    rel_threshold, num_ions_threshold
from pyms.Utils.IO import save_data

# read the raw data, and set thresholds
# filter width, maxima in 'points' is apex, scans to combine,
# minimum number of ions, greater than or equal to threshold,
# percentage ratio of ion intensity to max ion intensity, trim start, stop

andi_file = "/x/PyMS/data/gc01_0812_066.cdf"

# deconvolution and peak list filtering parameters
points = 3; scans = 1; n = 3; t = 3000; r = 2;

data = ANDI_reader(andi_file)

im = build_intensity_matrix_i(data)

# get the size of the intensity matrix
n_scan, n_mz = im.get_size()
print " Size of the intensity matrix is (n_scans, n_mz):", n_scan, n_mz

# smooth data
for ii in range(n_mz):
#    print "Working on IC#", ii+1
    ic = im.get_ic_at_index(ii)
    ic1 = savitzky_golay(ic)
    ic_smooth = savitzky_golay(ic1)
    ic_base = tophat(ic_smooth, struct="1.5m")
    im.set_ic_at_index(ii, ic_base)

# get the list of Peak objects
pl = BillerBiemann(im, points, scans)
#print "Number of Peaks found:", len(pl)

# trim by relative intensity
apl = rel_threshold(pl, r)

# trim by threshold
bpl = num_ions_threshold(apl, n, t)

# store peak list
store_peaks(bpl, "output/MixMA-5C-1.peaks")

print "Number of peaks stored", len(bpl)
