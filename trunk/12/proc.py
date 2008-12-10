"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.SavitzkyGolay import savitzky_golay

andi_file = "/x/proj.archive/proj/PyMS/data/pyms-data/a0806_140.CDF"
andi_data = ChemStation(andi_file)

tic = andi_data.get_tic()

tic1 = savitzky_golay(tic)

tic.write("output/tic.dat",minutes=True)
tic1.write("output/tic1.dat",minutes=True)

