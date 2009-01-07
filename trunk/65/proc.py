"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Alignment.Function import exprl2alignment
from pyms.Alignment.Function import align_with_tree
from pyms.Alignment.Class import PairwiseAlignment

# path to ANDI-MS data file
andi_file1 = "/x/proj.archive/proj/PyMS/data/a0806_077.CDF"
andi_file2 = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"

# get the intensity matrix and save to a file
andi_data1 = ChemStation(andi_file1)
andi_data2 = ChemStation(andi_file2)

# print the name of the ANDI-MS file
print "ANDI-MS data 1 filename:", andi_data1.get_filename()
print "ANDI-MS data 2 filename:", andi_data2.get_filename()

# get the entire intensity matrix
im1 = andi_data1.get_intensity_matrix()
im2 = andi_data2.get_intensity_matrix()

print "Dimensions of the intensity matrix 1 are:",len(im1),"x",len(im1[0])
print "Dimensions of the intensity matrix 2 are:",len(im2),"x",len(im2[0])

Gw =0.30

E1 = [im1,im2]
F1 = exprl2alignment(E1)
T1 = PairwiseAlignment(F1, Gw)
#A1 = align_with_tree(T1)
print "Job done"
