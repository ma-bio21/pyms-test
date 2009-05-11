"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.Function import build_intensity_matrix
from pyms.GCMS.Function import diff
from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader

andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data1 = ANDI_reader(andi_file)
data2 = JCAMP_reader(jcamp_file)

# Bin raw data to an IntensityMatrix, use default bin size of 1
im1 = build_intensity_matrix(data1)
im2 = build_intensity_matrix(data2)

# Check if 2 data sets are the same
diff(im1, im2)

