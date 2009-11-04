"""proc.py
"""

import sys
sys.path.append("/x/PyMS/")

from pyms.Flux.MassExtraction.Function import extract_mid

# -- input data ---
file_base = '/x/PyMS/data-0903/a0903_'
file_numbers = (297, 298, 299)
compound = 'Alanine'
ion = 190
rt = 411 # seconds

# -- parameters ---
mid_size = 6 # mid_size (n+1) is the number of masses (M, M+1, ..., M+n)
win_size = 4 # seconds

# extract mass isotopomer distribution vectors
extract_mid(file_base, file_numbers, compound, ion, rt, mid_size, win_size)
