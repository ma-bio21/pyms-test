"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.Window import window_smooth

# path to ANDI-MS data file
andi_file = "/home/current/proj/PyMS/pyms-data/a0806_140.CDF"

# get the intensity matrix
andi_data = ChemStation(andi_file)

# get TIC
tic = andi_data.get_tic()

# smooth TIC in two ways
tic1 = window_smooth(tic, window=3)
tic2 = window_smooth(tic, window=3, median=True)

