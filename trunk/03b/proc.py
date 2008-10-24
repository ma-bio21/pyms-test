"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.Experiment.IO import load_amdis_expr
from pyms.IO.ANDI.Class import Xcalibur

# path to AMDIS ELU data file
amdis_file = "/home/current/proj/PyMS/data/pyms-data/121107B_10.ELU"

# path to associated ANDI-MS data for AMDIS ELU data
# This parameter is optional and will use the full mass spectra for
# the peak and not the AMDIS generated mass spectra from the ELU file
andi_file = "/home/current/proj/PyMS/data/pyms-data/121107B_10.CDF"
andi_data = Xcalibur(andi_file)

expr = load_amdis_expr(amdis_file,andi_data)
peaks = expr.peaks

# the variable 'peaks' is a Python list
type(peaks)
print "The number of peaks is:", len(peaks)
