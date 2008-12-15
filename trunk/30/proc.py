"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat
from pyms.Noise.Function import analyze_noise 

# read the raw data
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"
data = ChemStation(andi_file)

# pre-processing
tic = data.get_tic()
tic1 = savitzky_golay(tic)
tic_bc = tophat(tic1, struct="1.5m")
noise = analyze_noise(tic_bc)

