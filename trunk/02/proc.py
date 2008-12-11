"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Peak.Class import Peak

# Create a peak with retention time 7.311 min and raw area of 33768615
# (these parameters were taken from the peak #3 from the ChemStation
# integration report file 'a0806_140.txt'). Convert retention time to
# seconds
p = Peak(7.311*60.0,33768615)

# print some properties of this peak
print "Peak retention time is", p.rt
print "Peak raw area is", p.raw_area
print "Peak normalized area is", p.norm_area
print "Peak mass spectrum is", p.mass_spectrum

# Set the peak mass spectrum. For this we need the raw data corresponding
# to 'a0806_140.txt'
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"
andi_data = ChemStation(andi_file)
p.set_mass_spectrum(andi_data)

# print mass spectrum and the m/z list on the screen. This will print 
# a bunch of numbers
print p.mass_spectrum
print p.mass_list

# p.mass_spectrum and p.mass_list must be of the same length
print len(p.mass_spectrum)
print len(p.mass_list)

# write mass spectrum to a file
p.write_mass_spectrum("output/ms.dat")

