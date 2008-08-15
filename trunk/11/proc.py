"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.Window import window_smooth

andi_file = "/home/current/proj/PyMS/pyms-data/a0806_140.CDF"
andi_data = ChemStation(andi_file)

tic = andi_data.get_tic()

tic1 = window_smooth(tic, window=5)
tic2 = window_smooth(tic, window=5, median=True)

print "Now applying time-specified window of 3 seconds"
tic9 = window_smooth(tic, window='3s')

tic.write("output/tic.dat",minutes=True)
tic1.write("output/tic1.dat",minutes=True)
tic2.write("output/tic2.dat",minutes=True)

