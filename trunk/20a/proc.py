"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.JCAMP.Function import JCAMP_reader

# read the raw data
jcamp_file = "/x/PyMS/data/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)

# raw data operations
print "minimum mass found in all data: ", data.get_min_mass()
print "maximum mass found in all data: ", data.get_max_mass()

# time
time = data.get_time_list()
print "number of retention times: ", len(time)
print "retention time of 1st scan: ", time[0], "sec"
print "index of 400sec in time_list: ", data.get_index_at_time(400.0)

# TIC
tic = data.get_tic()
print "number of scans in TIC: ", len(tic)
print "start time of TIC: ", tic.get_time_at_index(0), "sec"

# raw scans
scans = data.get_scan_list()

print "number of masses in 1st scan: ", len(scans[0])
print "1st mass value for 1st scan: ", scans[0].get_mass_list()[0]
print "1st intensity value for 1st scan: ", scans[0].get_intensity_list()[0]

print "minimum mass found in 1st scan: ", scans[0].get_min_mass()
print "maximum mass found in 1st scan: ", scans[0].get_max_mass()
