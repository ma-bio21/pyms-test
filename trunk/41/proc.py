"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.Utils.IO import save_data
from pyms.Simulator.Class import GCMS_simulator

s = GCMS_simulator(rt=['5.1m','21m',0.343], mz=[51,550,1])

rt = s.get_time_list()
mz = s.get_mass_list()
im = s.get_intensity_matrix()

print rt
print mz
print im

save_data("output/im.dat", im)
