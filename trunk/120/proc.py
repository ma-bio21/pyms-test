"""proc.py
"""

import sys
sys.path.append("/x/PyMS")

from pyms.MSlib.Function import load_nist, write_ms_lib, load_ms_lib, read_ms_lib

nist_file = "/x/PyMS/data/nist08_test.jca"
output_file = "output/mslib_object"

ms_lib = load_nist(nist_file)
                                           
write_ms_lib(ms_lib, output_file)
                                                                                     
lib = load_ms_lib(output_file)

read_ms_lib(lib)
