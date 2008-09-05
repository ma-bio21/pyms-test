"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.SavitzkyGolay import savitzky_golay

andi_file = "/home/current/proj/PyMS/pyms-data/a0806_140.CDF"
andi_data = ChemStation(andi_file)

tic = andi_data.get_tic()

tic1 = savitzky_golay(tic)

tic.write("output/tic.dat",minutes=True)
tic1.write("output/tic1.dat",minutes=True)

