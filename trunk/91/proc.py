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

# data_file_root = '/x/PyMS/data/'
data_file_root = '/home/projects/PyMS/data/0905/'
# data_file_names_file = '/x/PyMS/pyms-test/91/input/file_names.txt'
data_file_names_file = '/home/projects/PyMS/pyms-test/91/input/file_names.txt'

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

# read data file names

fp = open(data_file_names_file, 'r')
lines = fp.readlines()
data_file_names = []

for line in lines:
    data_file_names.append(line.strip())

# loop over file names

for file_name in data_file_names:

    # load raw data
    print '\n'
    andi_file = data_file_root+file_name+".CDF"
    data = ANDI_reader(andi_file)

    # create intensity matrix
    im = build_intensity_matrix_i(data)
    print 'built matrix'
    # process data file to extract MIDs
    for mids in mids_list:
        mids = extract_mid(file_name, im, mids, win_size, noise)

# write extracted MIDs to output file
print '\n',' -> Writing to file ', out_file
for mids in mids_list:       
    mids.write(out_file)
