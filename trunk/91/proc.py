"""proc.py
"""

import sys
sys.path.append("/x/PyMS/")

from pyms.Flux.MassExtraction.Function import extract_mid

# -- input data ---
file_base = '/home/projects/PyMS/data-0903/a0903_'
file_numbers = (297, 298, 299, 301, 302, 303, 304, 306, 307, 308, 253, 255, 256, 257, 258, 260, 261, 262, 263, 265, 266, 267, 268, 270, 271, 272, 273)
compound = 'Alanine'
ion = 190
rt = 411 # equals 6.85mins

# -- parameters ---
mid_size = 6 # mid_size is the total number of masses (M, M+1, ..., M+n), it equals n+1
win_size = 4 # seconds

# extract mass isotopomer distribution vectors
extract_mid(file_base, file_numbers, compound, ion, rt, mid_size, win_size)
