"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Experiment.Class import Experiment
from pyms.Peak.List.IO import read_chem_station_peaks
from pyms.Experiment.IO import dump_expr

# path to ANDI-MS data and annotated ChemStation peak files
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"
peak_file = "/x/proj.archive/proj/PyMS/data/a0806_140.txt.a"

# read the ANDI-MS data file and Chemstation peak report
data = ChemStation(andi_file)
peaks = read_chem_station_peaks(peak_file)

# the variable 'peaks' is a Python list
type(peaks)
print "The number of peaks is:", len(peaks)

# set the mass spectrum for each peak
for peak in peaks:
    peak.set_mass_spectrum(data)

# set up an experiment from this set of peaks
expr = Experiment("a0806_140", peaks)
expr.set_ref_peak("si")
expr.remove_blank_peaks()
expr.raw2norm_area()
expr.purge_peaks()
expr.sele_rt_range(["6.5m", "21m"])

# dump experiment to a file
dump_expr(expr, "output/a0806_140.pickle")

