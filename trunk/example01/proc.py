"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Utils.IO import save_data

andi_file = "/home/current/proj/PyMS/pyms-data/0510_217.CDF"

data = ChemStation(andi_file)

im = data.get_intensity_matrix()
ic = data.get_tic()

save_data("output/im.dat", im)

ic.write("output/ticm.dat", minutes=True)
ic.write("output/tics.dat", minutes=False)

