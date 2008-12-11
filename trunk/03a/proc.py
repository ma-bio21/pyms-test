"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.Experiment.IO import load_xcalibur_expr

# path to ANDI-MS data file and  annotated ChemStation peak file
andi_file = "/x/proj.archive/proj/PyMS/data/121107B_10.CDF"
peak_file = "/x/proj.archive/proj/PyMS/data/121107B_10_xcalibur_peaks.txt"

expr = load_xcalibur_expr(peak_file,andi_file)
peaks = expr.peaks

# the variable 'peaks' is a Python list
type(peaks)
print "The number of peaks is:", len(peaks)

