"""proc.py
"""

import sys
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation

andi_file = "/home/current/proj/PyMS/pyms-data/0510_217.CDF"

data = ChemStation(andi_file)

