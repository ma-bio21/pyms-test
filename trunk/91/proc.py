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
# data_file_nums = (297, 298, 299, 301, 302, 303, 304, 306, 307, 308, 253, 255, 256, 257, 258, 260, 261, 262, 263, 265, 266, 267, 268, 270, 271, 272, 273)

# out_file = '/x/PyMS/pyms-test/91/output/out.csv'
out_file = '/home/projects/PyMS/pyms-test/91/output/out.csv'

# set compound name, retention time, diagnostic ions and MID size
mids = MIDS('alanine', 411, [190], 6)

# -- end input data ---

# -- parameters ---
win_size = 4 # seconds
noise = 4000 #todo: estimate from data files
# -- end parameters ---

# extract mass isotopomer distribution vectors
mids = extract_mid(data_file_root, data_file_nums, mids, win_size, noise)

mids.write(out_file)
