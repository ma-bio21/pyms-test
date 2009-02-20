"""proc.py
"""

import sys
sys.path.append("/x/archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.Window import window_smooth

# read the raw data
andi_file = "/x/archive/proj/PyMS/data/a0806_140.CDF"
data = ChemStation(andi_file)

# get the TIC
tic = data.get_tic()

# apply window smoothing: mean and median, in both cases
# the window is 5 points
tic1 = window_smooth(tic, window=5)
tic2 = window_smooth(tic, window=5, median=True)

# nn example of how to specify window as a time string
# (3 seconds in this case)
tic9 = window_smooth(tic, window='3s')

# write mean and median smoothed TIC to a file
tic.write("output/tic.dat",minutes=True)
tic1.write("output/tic1.dat",minutes=True)
tic2.write("output/tic2.dat",minutes=True)

