"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.Experiment.Class import Experiment
from pyms.Experiment.IO import store_expr, load_expr
from pyms.Peak.Class import Peak
from pyms.Peak.IO import load_peaks
from pyms.Utils.IO import save_data

# test to create, store and re-load experiment
peak_list = load_peaks("../x02a/output/MixMA-5C-1.peaks")

expr = Experiment("MixMA-5C-1", peak_list)

store_expr("output/MixMA-5C-1.expt", expr)

# check stored
expr2 = load_expr("output/MixMA-5C-1.expt")

print "saved:", expr.get_name(), "peak list len:", len(expr.get_peak_list())
print "loaded:", expr2.get_name(), "peak list len:", len(expr2.get_peak_list())
