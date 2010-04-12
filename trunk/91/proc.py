"""proc.py
"""

import sys

sys.path.append("/x/PyMS/")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.MIDs.Function import parse_ion_defs, parse_data_defs
from pyms.MIDs.MassExtraction.Function import extract_mid

# -- input data ---
data_file_root = '/x/PyMS/data/'
ion_defs = 'input/ion_definitions'
data_defs = 'input/data_files'
out_file = 'output/out.csv'
# -- end input data ---

# -- input parameters ---
win_size = 4 # seconds, peak width is 1 to 1.5 win size 
noise = 4000 #relates to the threshold of signal after which peaks lose shape/width goes down
# -- end input parameters ---

# read in diagnostic ion info
mid_table_list = parse_ion_defs(ion_defs)

# read in data file names
data_files = parse_data_defs(data_defs)

# loop over file names and extract MIDs
for file_name in data_files:

    # load raw data
    print '\n'
    andi_file = data_file_root + file_name + ".CDF"
    data = ANDI_reader(andi_file)

    # create intensity matrix
    im = build_intensity_matrix_i(data)
    print ' -> Intensity matrix built'

    # process data file to fill empty MID tables
    for mid_table in mid_table_list:
        extract_mid(mid_table, file_name, im, win_size, noise)

# write filled MID tables, including any warnings, to out_file
print '\n',' -> Writing to file ', out_file
for mid_table in mid_table_list:       
    mid_table.write(out_file)

