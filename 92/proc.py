"""proc.py
"""

import sys
sys.path.append("/x/PyMS/")

from pyms.MIDs.Function import parse_mid_tables_file, parse_ion_file, write_mid_tables
from pyms.MIDs.MassCorrection.Function import correct_mdv, fract_labelling, \
    corr_unlabelled, overall_correction_matrix, correction_matrix, \
    c_mass_isotope_distr, mass_dist_vector

# -- input data ---
mid_tables_file = 'input/out.csv'
ion_file = 'input/ion_composition'
out_file = 'output/corrected-out.csv'
# -- end input data ---

# -- input parameters ---
f_unlabelled = 0.01 # correction factor for unlabelled biomass
# -- end input parameters ---

# parse input files
mid_table_list = parse_mid_tables_file(mid_tables_file)
mid_table_list = parse_ion_file(ion_file, mid_table_list)

# loop through MID tables and correct
for mid_table in mid_table_list:

    table_values = mid_table.get_values()
    atoms = mid_table.get_atoms()

    # correct mdv values 
    for file_name, mdv in table_values.iteritems():
        mdv = correct_mdv(mdv, atoms, f_unlabelled)
        # fill the MID table with mdv values
        mid_table.set_values(mdv, file_name)

# write corrected MID tables to out_file
print '\n',' -> Writing to file ', out_file
write_mid_tables(mid_table_list, out_file)








