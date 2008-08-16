"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.Window import window_smooth
from pyms.Baseline.TopHat import tophat

# load the data
andi_file = "/home/current/proj/PyMS/pyms-data/a0806_140.CDF"
andi_data = ChemStation(andi_file)

# get the TIC
tic = andi_data.get_tic()

# apply 5-point moving window smoothing
tic = window_smooth(tic, window=5)

# apply tophat baseline correction with 1 min structural element
tic2 = tophat(tic, struct="1m")

# save the original and processed TICs
tic.write("output/tic.dat",minutes=True)
tic2.write("output/tic2.dat",minutes=True)

