"""proc.py

This example uses the matplotlib library for plotting in Python

To use the Display class as shown in this script, the matplotlib
library must be installed. To check for this type "import matplotlib" 
in an interactive python session. 

The authors suggest the use of the TKAgg backend, which can be set in matplotlib
by changing the backend parameter in your matplotlibrc file.

The location of your matplotlibrc file can be found by typing
>>>import matplotlib
>>>matplotlib.matplotlib_fname()

in an interactive session
"""

import sys
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix

from pyms.Display.Function import plot_ics

# read the raw data as a GCMS_data object
andi_file = "/x/PyMS/data/gc01_0812_066.cdf"
data = ANDI_reader(andi_file)


# IntensityMatrix
# must build intensity matrix before accessing any intensity matrix methods.

# default, float masses with interval (bin interval) of one from min mass
print "default intensity matrix, bin interval = 1, boundary +/- 0.5"
im = build_intensity_matrix(data)


#
# IonChromatogram
#

# TIC from raw data
tic = data.get_tic()
# save TIC to a file



# get the ion chromatogram for some m/z channels (73, 147)
ic = im.get_ic_at_mass(73)
ic1 = im.get_ic_at_mass(147)
# create a list of ICs
ics = [tic, ic, ic1]


plot_ics(ics, ['TIC','73','147'], 'TIC and ICs for m/z = 73 & 147')

