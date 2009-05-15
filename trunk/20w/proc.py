"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader

# read the raw data
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
andi_file = "/x/PyMS/data/JP_MM_TOF.cdf"
data1 = ANDI_reader(andi_file)

# print info
data1.write("output/data")
#data1.info(print_scan_n=True)
data1.info()

