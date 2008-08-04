"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Peak.List.IO import read_chem_station_peaks

# path to ANDI-MS data file
andi_file = "/home/current/proj/PyMS/pyms-data/a0806_140.CDF"
# path to annotated ChemStation peak file
peak_file = "/home/current/proj/PyMS/pyms-data/a0806_140.txt.anno"

# read the ANDI-MS data file and Chemstation peak report
andi_data = ChemStation(andi_file)

andi_data.null_mass(73)
andi_data.null_mass(147)

peaks = read_chem_station_peaks(peak_file)

# set the mass spectrum for each peak
for peak in peaks:
    peak.set_mass_spectrum(andi_data)
    peak.crop_mass_spectrum(50, 540)

