"""proc.py
"""

import sys

# sys.path.append("/x/PyMS/")
sys.path.append("/home/projects/PyMS")

from pyms.Flux.Class import MIDS
from pyms.Flux.MassExtraction.Function import extract_mid

# -- input data ---
# data_file_root = '/x/PyMS/data-0903/a0903_'
data_file_root = '/home/projects/PyMS/data-0903/a0903_'
data_file_nums = (297, 298, 299)
# out_file = '/x/PyMS/data-0903/a0903_'
out_file = '/home/projects/PyMS/data-0903/output/output.csv' # todo: generalise

# set compound name, retention time, diagnostic ions and MID size
mids = MIDS('alanine', 411, [190], 6)

# -- parameters ---
win_size = 4 # seconds
noise = 4000 #todo: estimate from data files

# extract mass isotopomer distribution vectors
mids = extract_mid(data_file_root, data_file_nums, mids, win_size, noise)

mids.write(out_file)
