"""proc.py
"""

import sys
sys.path.append("/x/archive/proj/PyMS/")

from pyms.Experiment.IO import read_expr_list
from pyms.Peak.List.DPA.Function import exprl2alignment
from pyms.Peak.List.DPA.Class import PairwiseAlignment
from pyms.Peak.List.DPA.Function import align_with_tree

# define the input experiments list
input1 = "input1"

# within replicates alignment parameters
Dw = 2.5  # rt modulation [s]
Gw = 0.30 # gap penalty

# do the alignment
print 'Aligning input 1'
E1 = read_expr_list(input1)
F1 = exprl2alignment(E1)
T1 = PairwiseAlignment(F1, Dw, Gw)
A1 = align_with_tree(T1, min_peaks=2)

# save the alignment matrices
A1.write_csv('output/rt1.csv', 'output/area1.csv')

