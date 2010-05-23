"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

import sys, os, errno, string
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat
from pyms.Peak.Class import Peak
from pyms.Peak.Function import peak_sum_area
from pyms.Deconvolution.BillerBiemann.Function \
    import BillerBiemann, rel_threshold, num_ions_threshold
from pyms.Noise.Analysis import window_analyzer

# deconvolution and peak list filtering parameters
# 'pk_points' is the estimated number of points across signal peak
pk_points = 5
pk_scans = 2
n = 3
r = 1

#andi_file = "/x/PyMS/data/0605_549.CDF"
andi_file = "/x/PyMS/data/a0806_077.cdf"

# read raw data
data = ANDI_reader(andi_file)

# estimate noise level from the TIC, used later to 
# discern true signal peaks
tic = data.get_tic()
noise_level = window_analyzer(tic)

print " Building intensity matrix ...",
# build integer intensity matrix
im = build_intensity_matrix_i(data)
print " done."

# crop mass range to 50-540
im.crop_mass(50,540)

# ignore TMS ions 73 and 147
im.null_mass(73)
im.null_mass(147)

# get the size of the intensity matrix
n_scan, n_mz = im.get_size()

# loop over all IC: smoothing and baseline correction
print " Smoothing and baseline correction ...",

for ii in range(n_mz):
    ic = im.get_ic_at_index(ii)
    ic_smooth = savitzky_golay(ic)
    ic_base = tophat(ic_smooth, struct="1.5m")
    im.set_ic_at_index(ii, ic_base)

print " done."

# peak detection

print " Applying deconvolution ...",

# get the initial list of peak objects
pl = BillerBiemann(im, pk_points, pk_scans)

# trim by relative intensity
apl = rel_threshold(pl, r)

# trim by number of ions above threshold
peak_list = num_ions_threshold(apl, n, noise_level)

print " done."

print " [ Number of peaks found: %d ]" % ( len(peak_list) )

