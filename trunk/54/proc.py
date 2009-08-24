"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat

from pyms.Deconvolution.BillerBiemann.Function import BillerBiemann, \
    rel_threshold, num_ions_threshold

from pyms.Peak.Function import peak_sum_area

# read the raw data as a GCMS_data object
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
data = ANDI_reader(andi_file)

im = build_intensity_matrix_i(data)

n_scan, n_mz = im.get_size()

print "Intensity matrix size (scans, masses):", (n_scan, n_mz)

# noise filter and baseline correct
for ii in range(n_mz):
    ic = im.get_ic_at_index(ii)
    ic_smooth = savitzky_golay(ic)
    ic_bc = tophat(ic_smooth, struct="1.5m")
    im.set_ic_at_index(ii, ic_bc)

# Use Biller and Biemann technique to find apexing ions at a scan.
peak_list = BillerBiemann(im, points=9, scans=2)

# percentage ratio of ion intensity to max ion intensity
r = 2
# minimum number of ions, n
n = 3
# greater than or equal to threshold, t
t = 10000

# trim by relative intensity
pl = rel_threshold(peak_list, r)

# trim by threshold
new_peak_list = num_ions_threshold(pl, n, t)

print "Number of filtered peaks: ", len(new_peak_list)

# find and set areas
for peak in new_peak_list:
    rt = peak.get_rt()
    area = peak_sum_area(im, peak)
    peak.set_area(area)
