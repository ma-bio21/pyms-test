"""proc.py
"""

import sys
sys.path.append("/x/PyMS/")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.Noise.SavitzkyGolay import savitzky_golay

# read the raw data
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
data = ANDI_reader(andi_file)

# get the TIC
tic = data.get_tic()

tic1 = savitzky_golay(tic)

tic.write("output/tic.dat",minutes=True)
tic1.write("output/tic1.dat",minutes=True)

