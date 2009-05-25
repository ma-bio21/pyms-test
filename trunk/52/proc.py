"""proc.py
"""

import sys
sys.path.append("/x/PyMS/")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat

# read the raw data
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
data = ANDI_reader(andi_file)

# get the TIC
tic = data.get_tic()

# apply noise smoothing and baseline correction
tic = savitzky_golay(tic)
tic_bc = tophat(tic, struct="1.5m")

# save smoothed/baseline corrected TIC
tic.write("output/tic_bc.dat",minutes=True)

