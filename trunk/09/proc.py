"""proc.py
"""

import numpy

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.Isotope.MFRA.Functions import correction_matrix, mass_dist_vector, c_mass_isotope_distr
from pyms.Isotope.MFRA.Constants import nsi

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
f_unlablelled = 0.01
# -- end of input data --

# calculate n, this could work depending on the content of the  input file
n = len(mdv)-1

atom_symbols = atoms.keys() 

c_corr = numpy.eye(n+1) 
for a in atom_symbols:
    print '\n Calculating %s correction matrix' % ( a )
    m_corr = correction_matrix(n, atoms[a], nsi[a])
    c_corr = numpy.dot(c_corr,m_corr)

print('\nOverall correction matrix:')
print(c_corr)

# the exclusive mass isotope distribution of the carbon skeleton, mdv_alpha_star
mdv_alpha_star = c_mass_isotope_distr(mdv, c_corr)
print('\nNormalised mdv alpha star:')
print(mdv_alpha_star)

# correction for unlabelled biomass
mdv_unlabelled = mass_dist_vector(n, n, nsi['c'])
mdv_aa = (mdv_alpha_star - f_unlablelled * mdv_unlabelled)/(1 - f_unlablelled)
print('\nmdv_aa:')
print(mdv_aa)

# For [U-13C]glucose experiments, the fractional labelling (FL) of
# the different amino fragments should be equal to the labelling content of
# the input substrate (i.e. when 20% [U-13C]glucose is used, the FL should
# be 0.2 for all fragments).
mdv_aa = numpy.matrix(mdv_aa)
fl = (range(0,(n+1)) * mdv_aa) / (n * numpy.sum(mdv_aa))
print('\nFractional labelling FL:')
print(fl)


