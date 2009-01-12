"""proc.py
"""

import sys
sys.path.append("/home/qiaow/Desktop/pyms-read-only")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Alignment.Function import fma

# path to ANDI-MS data file
andi_file1 = "/home/qiaow/PyMS/pyms-data/a0806_077.CDF"
andi_file2 = "/home/qiaow/PyMS/pyms-data/a0806_140.CDF"

# import the GC-MS data
andi_data1 = ChemStation(andi_file1)
andi_data2 = ChemStation(andi_file2)

Gw =0.30

fma(andi_data1, andi_data2, Gw)

print "All done"