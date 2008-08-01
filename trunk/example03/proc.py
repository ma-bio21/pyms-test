"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Utils.IO import save_data

# path to ANDI-MS data file
andi_file = "/home/current/proj/PyMS/pyms-data/0510_217.CDF"

# read the ANDI-MS data
data = ChemStation(andi_file)

# get the intensity matrix and save to a file
im = data.get_intensity_matrix()
save_data("output/im.dat", im)

# get the TIC and save to a file
ic = data.get_tic()
ic.write("output/tic.dat")

