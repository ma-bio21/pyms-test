"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.libMS.JCAMP.IO import load_jcamp

ms_lib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp.broken"

records = load_jcamp(ms_lib_file)

for r in records:
    print r.name
    print r.mass_spectrum

