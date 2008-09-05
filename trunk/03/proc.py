"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Experiment.Class import Experiment
from pyms.Peak.List.IO import read_chem_station_peaks
from pyms.Experiment.IO import dump_expr

# path to ANDI-MS data file and  annotated ChemStation peak file
andi_file = "/home/current/proj/PyMS/pyms-data/a0806_140.CDF"
peak_file = "/home/current/proj/PyMS/pyms-data/a0806_140.txt.a"

# read the ANDI-MS data file and Chemstation peak report
andi_data = ChemStation(andi_file)
peaks = read_chem_station_peaks(peak_file)

# the variable 'peaks' is a Python list
type(peaks)
print "The number of peaks is:", len(peaks)

# set the mass spectrum for each peak
for peak in peaks:
    peak.set_mass_spectrum(andi_data)

# set up an experiment from this set of peaks
expr = Experiment("a0806_140", peaks)
expr.set_ref_peak("si")
expr.remove_blank_peaks()
expr.raw2norm_area()
expr.purge_peaks()
expr.sele_rt_range(["6.5m", "21m"])

# dump experiment to a file
dump_expr(expr, "output/a0806_140.pickle")
