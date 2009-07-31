"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader
from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import diff

# read the raw data
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"

data1 = ANDI_reader(andi_file)
data2 = JCAMP_reader(jcamp_file)

# trim data2 between scans 1000 and 2000
#data2.trim(begin=1000,end=2000)

diff(data1,data2)

