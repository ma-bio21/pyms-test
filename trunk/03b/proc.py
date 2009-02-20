"""proc.py
"""

import sys
sys.path.append("/x/archive/proj/PyMS/")

from pyms.Experiment.IO import load_amdis_expr
from pyms.IO.ANDI.Class import Xcalibur

# path to ANDI-MS data which was used to generate AMDIS ELU data.
andi_file = "/x/archive/proj/PyMS/data/121107B_10.CDF"
data = Xcalibur(andi_file)

# path to AMDIS ELU data file
amdis_file = "/x/archive/proj/PyMS/data/121107B_10.ELU"

# This full data is an optional argument. If available the full mass
# spectra for the peaks will be used, and not the AMDIS generated
# mass spectra from the ELU file
expr = load_amdis_expr(amdis_file,data)
peaks = expr.peaks

# the variable 'peaks' is a Python list
type(peaks)
print "The number of peaks is:", len(peaks)

