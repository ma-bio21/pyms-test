"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.Experiment.IO import load_amdis_expr,load_xcalibur_expr
from pyms.Peak.List.Metric import metric

# path to ANDI-MS data file and Xcalibur and AMDIS peak files
andi_file = "/x/proj.archive/proj/PyMS/data/121107B_10.CDF"
xcalibur_peaks = "/x/proj.archive/proj/PyMS/data/121107B_10_xcalibur_peaks.txt"
amdis_peaks = "/x/proj.archive/proj/PyMS/data/121107B_10.ELU"

amdis_expr = load_amdis_expr(amdis_peaks)
xcalibur_expr = load_xcalibur_expr(xcalibur_peaks, andi_file)

# compare peak lists, verbose
metric_result = metric(amdis_expr.peaks, xcalibur_expr.peaks, verbose=True)

