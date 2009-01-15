"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS")

import pyms.Alignment.Function
import pyms.Alignment.Class

from pyms.IO.ANDI.Class import ChemStation
from pyms.Alignment.Class import Alignment
from pyms.Alignment.Function import fma

# path to ANDI-MS data file
andi_file1 = "/x/proj.archive/proj/PyMS/data/a0806_077.CDF"
andi_file2 = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"

# import the GC-MS data
data1 = ChemStation(andi_file1)
data2 = ChemStation(andi_file2)
a1 = Alignment(data1)
a2 = Alignment(data2)
Gw =0.30

fma(a1, a2, Gw)

print "All done"