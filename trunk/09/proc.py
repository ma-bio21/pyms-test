"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.Isotope.MFRA.Function import fract_labelling, corr_unlabelled, \
    overall_correction_matrix, correction_matrix, c_mass_isotope_distr, \
    mass_dist_vector

# -- input data ---
# measured mass distribution vector
mdv = [737537, 179694, 88657, 178433]

# number of each atom type in the fragment
atoms = {
 'c' : 8,
 'o' : 2,
 'n' : 1,
 'h' : 26,
 'si' : 2,
 's' : 0
}

# correction for unlabelled biomass
f_unlabelled = 0.01
# -- end of input data --

# calculate n, this could work depending on the content of the  input file
n = len(mdv)-1

# the overall correction matrix
c_corr = overall_correction_matrix(n, mdv, atoms)
print('\n Overall correction matrix:')
print(c_corr)

# the exclusive mass isotope distribution of the carbon skeleton, mdv_alpha_star
mdv_alpha_star = c_mass_isotope_distr(mdv, c_corr)
print('\n Normalised mdv alpha star:')
print(mdv_alpha_star)

# correction for unlabelled biomass
mdv_aa = corr_unlabelled(n, mdv_alpha_star, f_unlabelled)
print('\n mdv_aa:')
print(mdv_aa)

# For [U-13C]glucose experiments, the fractional labelling (FL) of the different
# fragments should be equal to the labelling content of the input substrate 
# (i.e. when 20% [U-13C]glucose is used, the FL should be 0.2 for all fragments).
fl = fract_labelling(n, mdv_aa)
print('\n Fractional labelling FL: %s' % ( fl ))