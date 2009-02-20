"""proc.py
"""

import sys
sys.path.append("/x/archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat
from pyms.Noise.Function import analyze_noise 
from pyms.Peak.Detection.MinMax import minmax
from pyms.Peak.List.IO import write_peaks

# read the raw data
andi_file = "/x/archive/proj/PyMS/data/a0806_140.CDF"
data = ChemStation(andi_file)

# pre-processing
tic = data.get_tic()
tic1 = savitzky_golay(tic)
tic_bc = tophat(tic1, struct="1.5m")
noise = analyze_noise(tic_bc)
peaks = minmax(tic_bc, 1.5*noise, window="1.7s")

# write TIC and peaks
tic_bc.write("output/tic.dat")
write_peaks(peaks, "output/peaks.dat", verbose_level=1)

