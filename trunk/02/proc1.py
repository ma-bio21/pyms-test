"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.Peak.Class import Peak
p = Peak(360.0,123337)

print "Peak retention time is", p.rt
print "Peak raw area is", p.raw_area
print "Peak normalized area is", p.norm_area
print "Peak mass spectrum is", p.mass_spectrum


