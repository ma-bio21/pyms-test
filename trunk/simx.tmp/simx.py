"""
Provides a class to simulate mass spectra of mixtures
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

import math
import sys
import os

# TODO: is this the correct form, or is import numpy safer?
from numpy import *

from chromatogram import chromatogram
from mass_spectrum import mass_spectrum

# set path to pyms, use envirionment var PYMS_BASE or try two dirs up
try:
    PYMS_BASE = os.environ["PYMS_BASE"]
except KeyError:
    try:
        os.chdir("../..")
        PYMS_BASE = os.getcwd()
        sys.path.append(PYMS_BASE)
    except:
        PYMS_BASE = ""

# TODO: from pyms.Utils.Error import error
from pyms.Utils.Utils import is_int, is_number
# TODO: from pyms.Utils.IO import open_for_writing, close_for_writing

class Simx:

    """
    @summary: Simulate mass spectra of mixtures

        Simulates the data matrix X as a linear mixture of the pure
        component matrix C and pure mass spectra S

    @author: Andrew Isaac
    """

#% > plot(sum(D')) % plots TIC of data matrix with noise
#% > plot(sum(X')) % plots TIC of ideal data matrix

    # internals
    __numComponents_    = 100
    __numChromPoints_   = 3000
    __numChannels_      = 500
    __sigma_            = 0.01

    def __init__(self, numComponents=100, numChromPoints=3000, numChannels=500,
            sigma=0.01):

        """
        @summary: Simx(numComponents=100, numChromPoints=3000, numChannels=500,
            sigma=0.01)
        @param numComponents: Total number of components
        @type numComponents: Positive Integer
        @param numChromPoints: Number of chromatographic time points
        @type numChromPoints: Positive Integer
        @param numChannels: Number of m/z channels
        @type numChannels: Positive Integer
        @param sigma: Noise level (relative to max intensity=1.0)
        @type sigma: Positive Real, 0.0 <= sigma <= 1.0
        """

        # setting values does sanity testing
        self.setNumComponents(numComponents)
        self.setNumChromPoints(numChromPoints)
        self.setNumChannels(numChannels)
        self.setSigma(sigma)

    # parameter handling with sanity checking
    def setNumComponents(self, numComponents=100):
        if not is_int(numComponents):
            raise TypeError, "numComponents must be an integer"
        elif numComponents < 1:
            raise ValueError, "numComponents must be greater than 0"
        else:
            self.__numComponents_ = numComponents

    def getNumComponents(self):
        return self.__numComponents_

    def setNumChromPoints(self, numChromPoints=3000):
        if not is_int(numChromPoints):
            raise TypeError, "numChromPoints must be an integer"
        elif numChromPoints < 1:
            raise ValueError, "numChromPoints must be greater than 0"
        else:
            self.__numChromPoints_ = numChromPoints

    def getNumChromPoints(self):
        return self.__numChromPoints_

    def setNumChannels(self, numChannels=500):
        if not is_int(numChannels):
            raise TypeError, "numChannels must be an integer"
        elif numChannels < 1:
            raise ValueError, "numChannels must be greater than 0"
        else:
            self.__numChannels_ = numChannels

    def getNumChannels(self):
        return self.__numChannels_

    def setSigma(self, sigma=0.01):
        if not is_number(sigma):
            raise TypeError, "sigma must be a number"
        elif sigma < 0 or sigma > 1:
            raise ValueError, "sigma must be in the range [0,1]"
        else:
            self.__sigma_ = sigma

    def getSigma(self):
        return self.__sigma_

    def genComponents(self, numComponents=__numComponents_,
                      numChromPoints=__numChromPoints_):

        """
        @summary: Generate the matrix C as numComponents by numChromPoints
        @param numComponents: Total number of components
        @type numComponents: Positive Integer
        @param numChromPoints: Total number of chromatographic time points
        @type numChromPoints: Positive Integer
        @return: Component matrix
        @type: Real valued Matrix
        """

        #print "calculating C"

        # create matrix (as an array) of zeroed floats (doubles)
        __C_ = zeros((numComponents, numChromPoints), 'd')

        # Python and NumPy use zero indexing
#        for ii in range(numComponents):
#           ch = chromatogram(numChromPoints)
            # C = [C ch']
        # TODO: is this efficient?
        for ii in range(numComponents):
            ch = chromatogram(numChromPoints)
#            ch = random.uniform(0,1,(1,numChromPoints))
            __C_[ii,:] = ch

        return __C_

    def genSpectra(self, numComponents=__numComponents_,
                   numChannels=__numChannels_):

        """
        @summary: Generate the matrix S as numComponents by numChannels
        @param numComponents: Total number of components
        @type numComponents: Positive Integer
        @param numChannels: Number of m/z channels
        @type numChannels: Positive Integer
        @return: Spectra matrix
        @type: Real valued Matrix
        """
        print "calculating S"

        # create matrix (as an array) of zeroed floats (doubles)
        S = zeros((numComponents, numChannels), 'd')

        for ii in range(numComponents):
            m = mass_spectrum(numChannels)
#            m = random.uniform(0,1,(1,numChannels))
            S[ii,:] = m

        return S

    def genMixture(self, C, S):

        """
        @summary: Calculate the data matrix X as a linear mixture of components
        @param C: Component matrix
        @type C: Real valued Matrix
        @param S: Spectra matrix
        @type S: Real valued Matrix
        @return: Mixture matrix
        @type: Real valued Matrix
        """
        print "calculating X = C*S^T"
        # TODO matrix transpose and mult
        # X = C*S';
        X = dot(C.T,S)
        return X

    def addNoise(self, X):
        """
        @summary: Generate random noise
        @param X: Real valued Matrix
        @type X: Real valued Matrix
        @return: Input matrix with added noise
        @type: Real valued Matrix
        """
        print "generating noise"
        # TODO more matrix stuff
        # Nm = rand(size(X))*sigma;
        # D = X+Nm;
        Nm = random.uniform(0.0,1.0,X.shape)*self.__sigma_
        D = X+Nm
        return D

