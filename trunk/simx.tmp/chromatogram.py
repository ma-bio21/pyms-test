"""
Provides a function to simulate ion chromatogram of a pure component
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

## NB: personal preference for local variables to be hidden

# TODO: is there a way to define global consts?

import random
import numpy

from gaussian import gaussian

#function [v] = chromatogram(NT)
def chromatogram(numChromPoints):

    """
    Returns a simulated ion chromatogram of a pure component
    The ion chromatogram contains a single gaussian peak.
    The peak position is randomly chosen, but not to be closer
    to the edges for more than the fraction 'offset' of the
    total time domain.
    The peak width is randomly chosen between 'w1' and 'w2'.
    The peak intensity is randomly chosen between 0 and 1.
    """

    #% peak width limits
    w1 = 0.0005
    w2 = 0.0015

    #% peak position offset from the edges
    offset = 0.02
    d = offset
    g = 1-offset

    V = numpy.zeros((numChromPoints), 'd')

    # TODO: rand from [0,1] or [-1,1]?
    peak_width = w1 + (w2-w1)*random.random()
    peak_pos = d + (g-d)*random.random()
    peak_scale = random.random()

    for ii in range(numChromPoints):
        x = ii/numChromPoints
        V[ii] = gaussian(x,peak_pos,peak_width,peak_scale)

    return V
