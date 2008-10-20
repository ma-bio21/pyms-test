"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.Window import window_smooth
from pyms.Baseline.TopHat import tophat

# load the data
andi_file = "/home/current/proj/PyMS/data/pyms-data/a0806_140.CDF"
andi_data = ChemStation(andi_file)

# get the TIC
tic = andi_data.get_tic()

# apply 5-point moving window smoothing & baseline corrector
tic = window_smooth(tic, window=5)
tic_bc = tophat(tic, struct="1.5m")

# save the original and baseline corrected TICs
tic.write("output/tic.dat",minutes=True)
tic_bc.write("output/tic_bc.dat",minutes=True)

