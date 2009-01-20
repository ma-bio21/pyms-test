"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.JCAMP.Class import MSLib
from pyms.IO.ANDI.Class import ChemStation

ms_lib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp"
andi_file = "/x/proj.archive/proj/PyMS/data/a0806_140.CDF"

ms_lib = MSLib(ms_lib_file)

data = ChemStation(andi_file)
mass_list = data.get_mass_list()

ms_lib.set_for_search(mass_list)

for r in ms_lib.records:
    print r.name
    print r.mass_record
    print r.mass_spectrum

