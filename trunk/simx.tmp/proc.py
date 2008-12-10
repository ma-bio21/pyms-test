
#import sys, os
#sys.path.append("/x/proj.archive/proj/PyMS/")

from simx import Simx

# Test code

X = Simx()
C = X.genComponents()
S = X.genSpectra()
Y = X.genMixture(C,S)
print X.addNoise(Y)

