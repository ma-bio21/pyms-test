"""proc.py
"""

import sys

sys.path.append("/x/PyMS/")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.MIDs.Function import parse_ion_defs, parse_data_defs, write_mid_tables
from pyms.MIDs.MassExtraction.Function import extract_mid

# -- input data ---
data_file_root = '/x/PyMS/data/'
ion_defs = 'input/ion_definitions'
data_defs = 'input/data_files'
out_file = 'output/out.csv'
# -- end input data ---

# -- input parameters ---
time_win = 4 # seconds, peak width is 1 to 1.5 win size 
int_tresh = 4000 #relates to the threshold of signal after which peaks lose shape/peak width goes down
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
        extract_mid(mid_table, file_name, im, time_win, int_tresh)
        mid_table.set_values(mdv, file_name)

# write filled MID tables, including any warnings, to out_file
print '\n',' -> Writing to file ', out_file
write_mid_tables(mid_table_list, out_file)
