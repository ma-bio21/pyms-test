"""proc.py
"""

import sys
sys.path.append("/x/archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.SavitzkyGolay import savitzky_golay

andi_file = "/x/archive/proj/PyMS/data/a0806_140.CDF"
data = ChemStation(andi_file)

tic = data.get_tic()

tic1 = savitzky_golay(tic)

tic.write("output/tic.dat",minutes=True)
tic1.write("output/tic1.dat",minutes=True)

