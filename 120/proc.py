"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.MSlib.Function import load_nist
from pyms.MSlib.Function import write_ms_lib
from pyms.MSlib.Function import load_ms_lib
from pyms.MSlib.Function import read_ms_lib

nist_file = "/x/PyMS/data/nist08.jca"
output_file = "output/mslib_object"

ms_lib = load_nist(nist_file)
                                           
write_ms_lib(ms_lib, output_file)
                                                                                     
lib = load_ms_lib(output_file)

read_ms_lib(lib)
