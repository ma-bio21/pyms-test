"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/code/")

from pyms import IO 
from pyms import Utils 

andi_file = "/home/current/proj/PyMS/code/pyms-data/0510_217.CDF"

data = IO.ANDI.Class.ChemStation(andi_file)

im = data.get_intensity_matrix()
ic = data.get_tic()

Utils.IO.save_data("output/im.dat", im)

ic.write("output/ticm.dat", minutes=True)
ic.write("output/tics.dat", minutes=False)

