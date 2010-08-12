"""proc.py
"""

import sys
sys.path.append("/x/PyMS/")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix
from pyms.Noise.Window import window_smooth_im

# read the raw data
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
data = ANDI_reader(andi_file)

# build an intensity matrix object from the data
im = build_intensity_matrix(data)

# Use window averaging to smooth all IC's in the IM
print "Smoothing ..."
im_smooth = window_smooth_im(im, window=5, median=False)
print "Done"

# find the IC for derivatisation product ion before smoothing
ic = im.get_ic_at_index(73)

# find the IC for derivatisation product ion after smoothing
ic_smooth = im_smooth.get_ic_at_index(73)

ic.write("output/ic.dat",minutes=True)
ic_smooth.write("output/ic_smooth.dat",minutes=True)