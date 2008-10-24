"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.Experiment.IO import read_expr_list
from pyms.Peak.List.DPA.Function import exprl2alignment
from pyms.Peak.List.DPA.Class import PairwiseAlignment
from pyms.Peak.List.DPA.Function import align_with_tree

# define the input experiments list
input1 = "input1"
input2 = "input2"

# within replicates alignment parameters
Dw = 2.5  # rt modulation [s]
Gw = 0.30 # gap penalty

# do the alignment
print 'Aligning input 1'
E1 = read_expr_list(input1)
F1 = exprl2alignment(E1)
T1 = PairwiseAlignment(F1, Dw, Gw)
A1 = align_with_tree(T1, min_peaks=2)

print 'Aligning input 1'
E2 = read_expr_list(input2)
F2 = exprl2alignment(E2)
T2 = PairwiseAlignment(F2, Dw, Gw)
A2 = align_with_tree(T2, min_peaks=2)

# between replicates alignment parameters
Db = 10.0 # rt modulation
Gb = 0.30 # gap penalty

print 'Aligning input {1,2}'
T9 = PairwiseAlignment([A1,A2], Db, Gb)
A9 = align_with_tree(T9)

A9.write_csv('output/rt.csv', 'output/area.csv')

