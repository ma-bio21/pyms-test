"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.Window import window_smooth

# path to ANDI-MS data file
andi_file = "/home/current/proj/PyMS/pyms-data/a0806_140.CDF"

# load the raw data
andi_data = ChemStation(andi_file)

# get TIC
tic = andi_data.get_tic()

# moving window smoothing: mean & median smoothing
tic1 = window_smooth(tic, window=5)
tic2 = window_smooth(tic, window=5, median=True)

# save the original TIC and smoothed TICs
tic.write("output/tic.dat",minutes=True)
tic1.write("output/tic1.dat",minutes=True)
tic2.write("output/tic2.dat",minutes=True)

