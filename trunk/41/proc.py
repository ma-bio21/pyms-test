"""proc.py
"""

import sys
sys.path.append("/x/proj.archive/proj/PyMS/")

from pyms.MSlib.Function import load_jcamp

mslib_file = "/x/proj.archive/proj/PyMS/data/mslib.jcamp"

mslib = load_jcamp(mslib_file)

