"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.Experiment.IO import load_amdis_expr
from pyms.IO.ANDI.Class import Xcalibur

# path to AMDIS ELU data file
amdis_file = "/home/current/proj/PyMS/data/pyms-data/121107B_10.ELU"

# path to ANDI-MS data which was used to generate AMDIS ELU data.
andi_file = "/home/current/proj/PyMS/data/pyms-data/121107B_10.CDF"
andi_data = Xcalibur(andi_file)

# This full data is an optional argument. If available the full mass
# spectra for the peaks will be used, and not the AMDIS generated
# mass spectra from the ELU file
expr = load_amdis_expr(amdis_file,andi_data)
peaks = expr.peaks

# the variable 'peaks' is a Python list
type(peaks)
print "The number of peaks is:", len(peaks)

