"""proc.py
"""

import sys, os
sys.path.append("/home/current/proj/PyMS/")

from pyms.IO.ANDI.Class import ChemStation
from pyms.Experiment.Class import Experiment
from pyms.Peak.List.IO import read_chem_station_peaks
from pyms.Experiment.IO import dump_expr

# define path to data files
base_path = "/home/current/proj/PyMS/data/pyms-data/"

# define experiments to process
expr_codes = [ "a0806_140", "a0806_141", "a0806_142" ]

# loop over all experiments
for expr_code in expr_codes:

    # define the names of the peak file and the corresponding ANDI-MS file
    peak_file = os.path.join(base_path, expr_code + ".txt.a")
    andi_file = os.path.join(base_path, expr_code + ".CDF")

    # load ANDI-MS data and chemstation peak list
    andi_data = ChemStation(andi_file)
    peaks = read_chem_station_peaks(peak_file)

    # null ion chromatograms for m/z=73 and m/z=147. These masses
    # originate from the derivatiziing agent
    andi_data.null_mass(73)
    andi_data.null_mass(147)

    # loop over peaks and add mass spectrum
    for peak in peaks:
        peak.set_mass_spectrum(andi_data)
        peak.crop_mass_spectrum(50,540)

    # create an experiment object
    expr = Experiment(expr_code, peaks)

    # set the reference peak, remove blank peaks, create norm area
    # purge negative peaks, and select peaks from the range 6.5 min
    # to 21 min
    expr.set_ref_peak("si")
    expr.remove_blank_peaks("blank")
    expr.raw2norm_area()
    expr.purge_peaks()
    expr.sele_rt_range(["6.5m", "21m"])

    # dump experiment to a file
    dump_expr(expr, "output/" + expr_code + ".expr")

