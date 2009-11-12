"""proc.py
"""

import sys

# sys.path.append("/x/PyMS/")
sys.path.append("/home/projects/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.Flux.Class import MIDS
from pyms.Flux.MassExtraction.Function import extract_mid

# -- input data ---

# data_file_root = '/x/PyMS/data-0903/a0903_'
data_file_root = '/home/projects/PyMS/data-0903/a0903_'
# data_file_nums = (301,302,303)
data_file_nums = (297, 298, 299, 301, 302, 303, 304, 306, 307, 308, 253, 255, 256, 257, 258, 260, 261, 262, 263, 265, 266, 267, 268, 270, 271, 272, 273)

# input file
# in_file = '/x/PyMS/pyms-test/91/input/in.csv'
in_file = '/home/projects/PyMS/pyms-test/91/input/in.csv'

# output file
# out_file = '/x/PyMS/pyms-test/91/output/out.csv'
out_file = '/home/projects/PyMS/pyms-test/91/output/out.csv'

# -- end input data ---

# -- parameters ---

win_size = 4 # seconds
noise = 4000 #todo: estimate from data files

# -- end parameters ---

# read input file

fp = open(in_file, 'r')
lines = fp.readlines()
mids_list = []

for line in lines:

    # parse input file
    items =line.split(',')
    name = str(items[0])
    rt = float(items[1])*60 # convert to seconds
    ion = int(items[2])
    mid_size = int(items[3])

    # set compound name, retention time, diagnostic ions and MID size
    mids = MIDS(name, rt, ion, mid_size)

    # store mids in mids_list
    mids_list.append(mids)

fp.close()

# loop over files

for file_num in data_file_nums:

    # load raw data
    andi_file = data_file_root+str(file_num)+".CDF"
    data = ANDI_reader(andi_file)

    # create intensity matrix
    im = build_intensity_matrix_i(data)

    # process data file to extract MIDs
    for mids in mids_list:
        mids = extract_mid(str(file_num), im, mids, win_size, noise)

# write extracted MIDs to output file
print ' -> Writing to file ', out_file
for mids in mids_list:       
    mids.write(out_file)
