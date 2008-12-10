"""
Provides a function simulate pure mass spectrum given the number of m/z
channels N
"""

 #############################################################################
 #                                                                           #
 #    PyMS software for processing of metabolomic mass-spectrometry data     #
 #    Copyright (C) 2005-8 Vladimir Likic                                    #
 #                                                                           #
 #    This program is free software; you can redistribute it and/or modify   #
 #    it under the terms of the GNU General Public License version 2 as      #
 #    published by the Free Software Foundation.                             #
 #                                                                           #
 #    This program is distributed in the hope that it will be useful,        #
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
 #    GNU General Public License for more details.                           #
 #                                                                           #
 #    You should have received a copy of the GNU General Public License      #
 #    along with this program; if not, write to the Free Software            #
 #    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.              #
 #                                                                           #
 #############################################################################

#function [m] = mass_spectrum(N)

#%
#% Returns a simulated pure mass spectrum given the number
#% of m/z channels N
#%
#% A mass spectrum contains between 1 and N/10 components
#% (the precise number is randomly chosen), with random
#% intensity in range 0-1.
#%

import random
import numpy
import math

def mass_spectrum(numChannels):
    #% initialize the m/z vector
    M = numpy.zeros((numChannels), 'd')

    #% the number of non-zero m/z values
    # NB: P < numChannels
    P = math.ceil((numChannels/10)*random.random());

    #% generate mass spectrum
    rp = range(numChannels)
    random.shuffle(rp)
    for ii in range(P):
        kk = rp[ii]
        M[kk] = random.random()

    return M
