"""proc.py
"""

import sys
sys.path.append("/x/PyMS/")

from pyms.GCMS.Function import build_intensity_matrix
from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.Peak.Class import Peak

##TODO: data file is different, get new peak values!!!

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
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
data = ANDI_reader(andi_file)

# Bin raw data to an IntensityMatrix, use default bin size of 1
im = build_intensity_matrix(data)

p.set_mass_spectrum(im)

# print mass spectrum and the m/z list on the screen. This will print
# a bunch of numbers
print p.mass_spectrum
print p.mass_list

# p.mass_spectrum and p.mass_list must be of the same length
print len(p.mass_spectrum)
print len(p.mass_list)

# write mass spectrum to a file
p.write_mass_spectrum("output/ms.dat")

# peaks can also operate on a single ion chromatogram.
# A peak has a Mass Spectrum or a ion chromatogram mass, but NOT both.
print "If peak has a mass spectrum, then the ion chromatogram mass is: ", \
p.get_ic_mass()

# setting an ion chromatogram mass
p.set_ic_mass(73)
# clears the mass spectrum
print "if peak has an ion chronatogram mass, then the mass " \
"spectrum is: ", p.mass_spectrum
