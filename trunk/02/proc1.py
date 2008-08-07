"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.Peak.Class import Peak

# create a peak with retention time 360.0 s and raw area of 123337.0
p = Peak(5.553*60.0,2759280)

# print some properties of this peak
print "Peak retention time is", p.rt
print "Peak raw area is", p.raw_area
print "Peak normalized area is", p.norm_area
print "Peak mass spectrum is", p.mass_spectrum

