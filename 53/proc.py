"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader
from pyms.GCMS.Function import build_intensity_matrix
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat
from pyms.Utils.IO import dump_object

# read the raw data as a GCMS_data object
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)

# Build intensity matrix, required before accessing any intensity matrix
# methods. Use defaults, float masses with interval (bin size) of one from
# min mass
print "building intensity matrix with bin interval=1"
im = build_intensity_matrix(data)

# save the pre-processed intensity matrix
print " Dumping the original intensity matrix"
dump_object(im, "output/im-orig.dump")

# get the size of the intensity matrix
n_scan, n_mz = im.get_size()
print " Size of the intensity matrix is (n_scans, n_mz):", n_scan, n_mz

# process data
print " Processing ICs"

for ii in range(n_mz):
    print "Working on IC#", ii+1
    ic = im.get_ic_at_index(ii)
    ic_smooth = savitzky_golay(ic)
    ic_bc = tophat(ic_smooth, struct="1.5m")
    im.set_ic_at_index(ii, ic_bc)

# save the pre-processed intensity matrix
print " Dumping the pre-processed intensity matrix"
dump_object(im, "output/im-proc.dump")

