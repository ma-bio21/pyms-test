"""proc.py
"""

import sys, os
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat
from pyms.Peak.Class import Peak
from pyms.Peak.IO import store_peaks
from pyms.Deconvolution.BillerBiemann.Functions import BillerBiemann, \
    rel_threshold, num_ions_threshold
from pyms.Utils.IO import save_data

from pyms.Experiment.Class import Experiment
from pyms.Experiment.IO import store_expr, load_expr



# define path to data files
base_path = "/x/PyMS/data/"

# define experiments to process
#expr_codes = [ "a0806_077", "a0806_078", "a0806_079" ]
expr_codes = [ "a0806_140", "a0806_141", "a0806_142" ]

# deconvolution and peak list filtering parameters
points = 3; scans = 1; n = 3; t = 3000; r = 2;

# loop over all experiments
for expr_code in expr_codes:

    print "Processing", expr_code

    # define the names of the peak file and the corresponding ANDI-MS file
    andi_file = os.path.join(base_path, expr_code + ".CDF")

    data = ANDI_reader(andi_file)

    im = build_intensity_matrix_i(data)

    # get the size of the intensity matrix
    n_scan, n_mz = im.get_size()
    #print " Size of the intensity matrix is (n_scans, n_mz):", n_scan, n_mz

    # smooth data
    for ii in range(n_mz):
    #    print "Working on IC#", ii+1
        ic = im.get_ic_at_index(ii)
        ic1 = savitzky_golay(ic)
        ic_smooth = savitzky_golay(ic1)
        ic_base = tophat(ic_smooth, struct="1.5m")
        im.set_ic_at_index(ii, ic_base)

    # get the list of Peak objects
    pl = BillerBiemann(im, points, scans)
    #print "Number of Peaks found:", len(pl)

    # trim by relative intensity
    apl = rel_threshold(pl, r)

    # trim by threshold
    peak_list = num_ions_threshold(apl, n, t)

    # ignore TMS ions and use same mass range for all experiments
    for peak in peak_list:
        peak.crop_mass(50,540)
        peak.null_mass(73)
        peak.null_mass(147)

    # create an experiment
    expr = Experiment(expr_code, peak_list)

    # use same time range for all experiments
    expr.sele_rt_range(["6.5m", "21m"])

    store_expr("output/"+expr_code+".expr", expr)
